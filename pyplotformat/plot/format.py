from matplotlib import pyplot as plt
import matplotlib.ticker as mticker
from .default_values import _default_colors, _MAX_LABEL_SIZE

import os
from matplotlib import pyplot as plt
from pathlib import Path
from textwrap import wrap


class Format():
    '''Format object which contains methods for formatting and writing matplotlib figures

    This class can be initialised with global parameters that will affect the entire figure.
    The created class can then be used to format multiple figures with these parameters.

    Parameters
    ----------
    shape : str, optional
        Figure shape as it should appear in a document. Options are 'single', 'double' and 'large',
        which correspond to 8cm x 7cm, 16cm x 7cm and 16cm x 14cm respectively. These sizes should
        take up half or all of the text width of a A4 document with 1" margins. (default value is 'single')
    fontsize : float, optional
        Font size for the text on the figure in point (1/72"). This setting defines the MEDIUM_SIZE
        attribute of the class. (default value is 10.0)
    saveloc : str, optional
        Directory location for plot objects to be saved to. (default value is '.')

    Attributes
    ----------
    shape : str
        Figure shape as it should appear in a document. Options are 'single', 'double' and 'large',
        which correspond to 8cm x 7cm, 16cm x 7cm and 16cm x 14cm respectively. These sizes should
        take up half or all of the text width of a A4 document with 1" margins.
    fontsize : float
        Font size for the text on the figure in point (1/72"). This setting defines the MEDIUM_SIZE
        attribute of the class.
    saveloc : str
        Directory location for plot objects to be saved to.
    SMALL_SIZE : float
        Size for small font text, equals 0.8*fontsize
    MEDIUM_SIZE : float
        Size for standard plot text, equals fontsize
    LARGE_SIZE : float
        Size fot large plot text, equals 1.2*fontsize
    defaultfont : Dict
        Matplotlib kwargs dict for font. Describes default font family and size
    axesfont : Dict
        Matplotlib kwargs dict for font. Describes font for axes labels
    titlefont : Dict
        Matplotlib kwargs dict for font. Describes font for title.
    tickfont : Dict
        Matplotlib kwargs dict for font. Describes font for axes ticks
    legendfont : Dict
        Matplotlib kwargs dict for font. Describes font for legends
    '''
    def __init__(   self, 
                    shape="single", 
                    fontsize=10,
                    saveloc="."
                ) -> None:
        

        self.shape      = shape
        self.saveloc    = saveloc
        self.fontsize   = fontsize
        
            
        self.SMALL_SIZE = fontsize*0.8
        self.MEDIUM_SIZE = fontsize
        self.BIGGER_SIZE = fontsize*1.2

        self.defaultfont = {"family":   "Times New Roman",
                            "size":     self.MEDIUM_SIZE,
                            }
        
        self.axesfont = dict(self.defaultfont)

        self.titlefont = dict(self.defaultfont)
        self.titlefont['size'] = self.BIGGER_SIZE

        self.tickfont = dict(self.defaultfont)

        self.legendfont = dict(self.defaultfont)

        self.figure = None
        self.axes = None

    
        self.defaultFormatOpts = {  'xlabel':           None,
                                    'ylabel':           None,
                                    'title':            None,
                                    'show':             False,
                                    'color':            None,
                                    'shortlabel':       None,
                                    'annotate':         False,
                                    'blackline':        False,
                                    'lxpad':            1.0,
                                    'lypad':            1.1,
                                    'uxpad':            1.0,
                                    'uypad':            1.1,
                                    'xylim':            None,
                                    'xscale':           None,
                                    'yscale':           None
                                                            }
        

    def _parseInput(self, 
                    figure, 
                    **kwargs) -> dict:

        # Assign figure and axes to object attributes
        self.figure = figure
        if len(self.figure.get_axes()) == 1:
            self.axes = self.figure.get_axes()[0]
        else:
            raise ValueError("Figure contains multiple axes. Only figures with one axes object are supported")

        # Parse optional arguments or assign default values
        for key, value in self.defaultFormatOpts.items():
            if key not in kwargs:
                kwargs[key] = value

        return kwargs

    def _formatFigSize(self, 
                       **kwargs):

        # Set figsize
        # ====================================================================================================
        if self.shape == "single":
            self.figure.set_size_inches(3.14961, 2.756) # 8cm x 7cm
        elif self.shape == "double":
            self.figure.set_size_inches(6.29921, 2.756) # 16cm x 7cm
        elif self.shape == "large":
            self.figure.set_size_inches(6.29921, 5.512) # 16cm x 14cm
        else:
            print("Plotter warning: shape attribute: {} not recognized, defaulting to \"single\".")
            self.figure.set_size_inches(3.14961, 3.14961) # 8cm x 8cm


    def _formatAxesLabels(self, 
                          **kwargs):
        
        # Set label and titles
        # ====================================================================================================
        if kwargs['xlabel'] is not None:
            self.axes.set_xlabel(kwargs['xlabel'], **self.axesfont)
        if kwargs['ylabel'] is not None:
            self.axes.set_ylabel(kwargs['ylabel'], **self.axesfont)
        if kwargs['title'] is not None:
            self.axes.set_suptitle(kwargs['title'], **self.titlefont)

    
    def _formatTicks(self,  
                     **kwargs):

        # Set tick formatting
        # ====================================================================================================
        ticks_loc = self.axes.get_xticks().tolist()
        self.axes.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))
        ticks_loc = self.axes.get_yticks().tolist()
        self.axes.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))

        self.axes.set_xticklabels(self.axes.get_xticks(), **self.tickfont)
        self.axes.set_yticklabels(self.axes.get_yticks(), **self.tickfont)
        #self.axes.tick_params(axis='both', **self.tickfont)


    def _formatLineColors(self, 
                          **kwargs):

        # Set line colors
        # ====================================================================================================
        if kwargs['blackline']:
            color_val = ["#000000"]*len(self.axes.get_lines())
        else:
            color_val = _default_colors
        if kwargs['color'] is not None:
            if len(kwargs['color']) != len(self.axes.get_lines()):
                raise ValueError("Length of specified color array should be equal to number of lines in given matplotlib.pyplot.Axes object")
            for ii, col in enumerate(kwargs['color']):
                color_val[ii] = col
        
        for ii, line in enumerate(self.axes.get_lines()):
            if color_val[ii] is not None:
                line.set_color(color_val[ii])

    
    def _formatLineAnnotation(self, 
                              **kwargs):

        # Add line annotation
        # ====================================================================================================
        if kwargs['annotate']:
            if len(kwargs['shortlabel']) != len(self.axes.get_lines()):
                raise ValueError("Length of specified annotation array should be equal to number of lines in given matplotlib.pyplot.Axes object")
            for line, name in zip(self.axes.get_lines(), kwargs['shortlabel']):
                y = line.get_ydata()[-1]
                self.axes.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(),
                                xycoords=self.axes.get_yaxis_transform(), textcoords="offset points",
                                size = 10, va="center", family="Times New Roman")

    
    def _formatAxesLimits(self, 
                          **kwargs):

        # Set axis limits
        # ====================================================================================================

        if kwargs['xylim'] is None:
            xmin = 1e20
            xmax = 1e-20
            ymin = 1e20
            ymax = 1e-20
            for line in self.axes.get_lines():
                if min(line.get_xdata()) < xmin:
                    xmin = min(line.get_xdata())
                if max(line.get_xdata()) > xmax:
                    xmax = max(line.get_xdata())
                if min(line.get_ydata()) < ymin:
                    ymin = min(line.get_ydata())
                if max(line.get_ydata()) > ymax:
                    ymax = max(line.get_ydata())

            
            self.axes.set_xlim(kwargs['lxpad']*xmin, kwargs['uxpad']*xmax)
            self.axes.set_ylim(kwargs['lypad']*ymin, kwargs['uypad']*ymax)
        else:
            self.axes.set_xlim(kwargs['xylim'][0], kwargs['xylim'][1])
            self.axes.set_ylim(kwargs['xylim'][2], kwargs['xylim'][3])

    
    def _formatAxesScale(self,  
                         **kwargs):

        # Scale for axes
        # ====================================================================================================
        if kwargs['xscale'] is not None:
            self.axes.set_xscale(kwargs['xscale'])
        if kwargs['yscale'] is not None:
            self.axes.set_yscale(kwargs['yscale'])

    
    def _formatTightLayout(self, 
                           **kwargs):

        xt = self.axes.get_xticks()
        if kwargs['xylim'] is not None:
            xt = [t for t in xt if t >= kwargs['xylim'][0] and t <= kwargs['xylim'][1]]


    def _display(self, 
                 **kwargs):

        if kwargs['show']:
            plt.show()
