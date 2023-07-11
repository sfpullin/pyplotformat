import os
from matplotlib import pyplot as plt
from pathlib import Path
from typing import Tuple
from textwrap import wrap
from pypdf import PdfWriter, PdfReader

from .textlegend import TextLegend, TextLegendHandler

_default_colors = [ '#e31a1c', '#1f78b4', '#33a02c',
                    '#ff7f00', '#6a3d9a', '#b15928',
                    '#fb9a99', '#a6cee3', '#b2df8a', 
                    '#fdbf6f', '#cab2d6', '#ffff99'
                    ]

_MAX_LABEL_SIZE = 24


#TODO: Eventually need a main class with all basic functions then create 
#       new classes that can deal with different plot types (polar, etc.)

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


        return


    def __call__(   self,
                    figure : plt.Figure,
                    axes : plt.Axes,
                    xlabel : str = None,
                    ylabel : str = None,
                    title  : str = None,
                    show   : bool = False,
                    color : list = None,
                    shortlabel : list = None,
                    label : list = None,
                    separatelegend : bool = False,
                    ncol = 4,
                    annotate : bool = False,
                    blackline : bool = False,
                    lxpad : float = 1.0,
                    uxpad : float = 1.0,
                    lypad : float = 1.1,
                    uypad : float = 1.1,
                    xylim: list = None
                ) -> Tuple[plt.Figure, plt.Axes]:
        '''Format figure according to class attributes and specified or default parameters.

        Format an matplotlib figure with data already plotted. Returns the formatted plots and
        optionally a separate legend figure. This method can be called using *objectname()*.
        
        Parameters
        ----------
        figure : matplotlib.pyplot.Figure
            Matplotlib `Figure` object with data plotted.
        axes : matplotlib.pyplot.Axes
            Matplotlib `Axes` object with data plotted
        xlabel : str, optional
            Label for the x-axis. (default value is None, will leave empty axis)
        ylabel : str, optional
            Label for the y-axis. (default value is None, will leave empty axis)
        title : str, optional
            Title of the plot. (default value is None, will leave empty title)
        show : bool, optional
            If `True` will show the plot before it is returned using `matplotlib.pyplot.show()`
        color : list, optional
            List of colors defined by strings (either matplotlib aliases or hex codes) with a length equal
            to the number of lines. This can be used to override the default color scheme. A subset of lines 
            can keep the default color scheme by leaving the corresponding list position with a value of `None`.
            (default value is `None`, which uses default color scheme)
        shortlabel : list, optional
            List of strings that can be placed at the rightmost edge of each line to help define it. This label
            will replace the legend handle. Useful for plots that do not use color to distinguish between lines.
            Labels should be between 1 and 3 characters. (default value is None)
        label : list, optional
            List of strings which define the legend labels for each line. Must be specified in order of lines in
            the `Axes` object. (default value is None, no legend will be produced)
        separatelegend : bool, optional
            If `True` will produce a 3rd output which gives a figure for a separate legend. This option should make 
            legend placement in a document a more simple process. If `False` a legend will be placed on the figure 
            but outside of the plot. The figure size will be adjusted to include the legend (works best for 'single' 
            plots). (default value is `False`)
        ncol : int, optional
            Number of columns in a separate legend if it is requested. Columns greater than 1 will produce 'flatter'
            legends which are more suitable for placing above plots in documents. (defualt calue is 4)
        annotate : bool, optional
            If `True` this option will enable short labels placed at the rightmost edge of each line to help define 
            it. If `False` short labels will not be used. (default `False`)
        blackline : bool, optional
            If `True` all lines will be coloured black. If `False` the default colour scheme will be used (or those 
            specified by the color parameter). (default value is `False`)
        lxpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the left edge of the line. (default value is 1.0) 
        uxpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the left edge of the line. (default value is 1.0)
        lypad : float, optional
            Multiplier for the extra whitespace inside of the axes from the lowest point of the line. (default value is 1.1) 
        uypad : float, optional
            Multiplier for the extra whitespace inside of the axes from the highest point of the line. (default value is 1.1)
        xylim : list, optional
            If not None, this value overrides the default axis limits set by the padding variables. (default value is None)
        
        Returns
        -------
        figure : matplotlib.pyplot.Figure
            matplotlib `Figure` object with formatting applied.
        axes : matplotlib.plyplot.Axes
            matplotlib `Axes` object with formatting applied.
        legend : matplotlib.pyploy.Figure
            matplotlib `Figure` object containing legend if parameter `separatelegend` was set to `True`
        '''

        # Set figsize
        # ====================================================================================================
        if self.shape == "single":
            if label is not None and not separatelegend:
                figure.set_size_inches(4.72441, 2.756) # 12cm x 7cm
            else:
                figure.set_size_inches(3.14961, 2.756) # 8cm x 7cm
        elif self.shape == "double":
            if label is not None and not separatelegend:
                figure.set_size_inches(7.87402, 2.756) # 20cm x 7cm
            else:
                figure.set_size_inches(6.29921, 2.756) # 16cm x 7cm
        elif self.shape == "large":
            if label is not None and not separatelegend:
                figure.set_size_inches(7.87402, 5.512) # 20cm x 14cm
            else:
                figure.set_size_inches(6.29921, 5.512) # 16cm x 14cm
        else:
            print("Plotter warning: shape attribute: {} not reckognized, defaulting to \"single\".")
            figure.set_size_inches(3.14961, 3.14961) # 8cm x 8cm
        
        # Set label and titles
        # ====================================================================================================
        if xlabel is not None:
            plt.xlabel(xlabel, **self.axesfont)
        if ylabel is not None:
            plt.ylabel(ylabel, **self.axesfont)
        if title is not None:
            plt.suptitle(title, **self.titlefont)

        # Set tick formatting
        # ====================================================================================================
        plt.xticks(**self.tickfont)
        plt.yticks(**self.tickfont)

        # Set line colors
        # ====================================================================================================
        if blackline:
            color_val = ["#000000"]*len(axes.get_lines())
        else:
            color_val = _default_colors
        if color is not None:
            if len(color) != len(axes.get_lines()):
                raise ValueError("Length of specified color array should be equal to number of lines in given matplotlib.pyplot.Axes object")
            for col, ii in enumerate(color):
                color_val[ii] = col
        
        for ii, line in enumerate(axes.get_lines()):
            line.set_color(color_val[ii])

        # Add line annotation
        # ====================================================================================================
        if annotate:
            if len(shortlabel) != len(axes.get_lines()):
                raise ValueError("Length of specified annotation array should be equal to number of lines in given matplotlib.pyplot.Axes object")
            for line, name in zip(axes.get_lines(), shortlabel):
                y = line.get_ydata()[-1]
                axes.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(),
                                xycoords=axes.get_yaxis_transform(), textcoords="offset points",
                                size = 10, va="center", family="Times New Roman")

        # Set line labels
        # ====================================================================================================
        if label is not None and not separatelegend:
            for line, name in zip(axes.get_lines(), label):
                line.set_label('\n'.join(wrap(name, _MAX_LABEL_SIZE)))
        
        # Modify legend to include line labels
        # ====================================================================================================
        if annotate and not separatelegend:
            obj = []
            legend_map = {}
            for line, slab in zip(axes.get_lines(), shortlabel):
                obj.append( TextLegend(slab, line.get_color()) )
            for o in obj:
                legend_map[o] = TextLegendHandler()

            leg = axes.legend(obj, label, handler_map=legend_map, prop=self.legendfont, loc="center left", bbox_to_anchor=(1, 0.5, 1.5748,0))
            leg.get_frame().set_edgecolor("black")

        else:
            if label is not None and not separatelegend:
                leg = axes.legend(prop=self.legendfont, loc="center left", bbox_to_anchor=(1, 0.5, 1.5748,0))
                leg.get_frame().set_edgecolor("black")


 
        # Set axis limits
        # ====================================================================================================

        if xylim is None:
            xmin = 1e20
            xmax = 1e-20
            ymin = 1e20
            ymax = 1e-20
            for line in axes.get_lines():
                if min(line.get_xdata()) < xmin:
                    xmin = min(line.get_xdata())
                if max(line.get_xdata()) > xmax:
                    xmax = max(line.get_xdata())
                if min(line.get_ydata()) < ymin:
                    ymin = min(line.get_ydata())
                if max(line.get_ydata()) > ymax:
                    ymax = max(line.get_ydata())

            
            axes.set_xlim(lxpad*xmin, uxpad*xmax)
            axes.set_ylim(lypad*ymin, uypad*ymax)
        else:
            
            axes.set_xlim(xylim[0], xylim[1])
            axes.set_ylim(xylim[2], xylim[3])

        
        # Add padding legend
        # ====================================================================================================
        # Hack to get constant width legend area. If actual legend is bigger than padding legend then it will 
        # wrap

        xt = axes.get_xticks()

        if label is not None and not separatelegend:
            pad_leg = plt.legend([" "*_MAX_LABEL_SIZE], loc="center left", bbox_to_anchor=(1, 0.2, 1.5748,0), frameon=False)
            pad_leg.legendHandles[0].set_visible(False)

            figure.add_artist(leg)


        # Add serarate legend as output
        # ====================================================================================================
        if separatelegend:
            
            lines = axes.get_lines()

            figlegend = plt.figure(figsize=(3.14961, 3.14961))

            if annotate:
                obj = []
                legend_map = {}
                for line, slab in zip(axes.get_lines(), shortlabel):
                    obj.append( TextLegend(slab, line.get_color()) )
                for o in obj:
                    legend_map[o] = TextLegendHandler()
            
                leg = figlegend.legend(obj, label, handler_map=legend_map, prop=self.legendfont, loc="center", ncol=ncol)
                leg.get_frame().set_edgecolor("black")
                figlegend.tight_layout()
            
            else:
                leg = figlegend.legend(lines, label, prop=self.legendfont, loc="center", ncol=ncol)
                leg.get_frame().set_edgecolor("black")
                figlegend.tight_layout()


        # Set tight layout
        # ====================================================================================================
        
        figure.tight_layout()

        axes.set_xticks(xt)

        if show:
            plt.show()

        if not separatelegend:
            return figure, axes, None
        else:
            return figure, axes, figlegend

    def write(  self,
                filename : str,
                figure : plt.Figure,
                axes : plt.Axes,
                legend : plt.Figure = None
            ) -> None:
        '''Write formatted figure objects to PDF file.
        
        Write matplotlib `Figure` and `Axes` objects to .pdf files including an optional
        legend parameter if one is creeated as a separate figure object. The file save
        location will depend on the `saveloc` attribute supplied to this class on creation
        and the string provided to this method as a parameter.

        Parameters
        ----------
        filename : str
            Name of the file for the figure .pdf. Extension is not required
        figure : matplotlib.pyplot.Figure
            Matplotlib `Figure` object to be printed.
        axes : matplotlib.pyplot.Axes
            Matplotlib `Axes` object to be printed.
        legend : Matplotlib.pyplot.Figure
            Matplotlib `Figure` object containing a legend if one was createed separately.
            (default value is `None`)
        '''

        fname = os.path.join(self.saveloc, Path(filename).with_suffix(".pdf"))

        figure.savefig(fname, dpi='figure', bbox_inches="tight")
        
        if len(axes.get_legend_handles_labels()[0]) != 0 and legend is None:
            
            reader = PdfReader(fname)
            writer = PdfWriter()

            maxlen = max([len(label) for label in axes.get_legend_handles_labels()[1]])
            
            labelsize = min(_MAX_LABEL_SIZE, maxlen)
            labelfrac = labelsize/_MAX_LABEL_SIZE

            fz = (1/3 - (1.222 - 0.522*labelfrac)/12) - labelfrac*3.1/12 # Empirically derived formula

            page = reader.pages[0]
            page.mediabox.upper_right = ( 
                page.mediabox.right * (1 - fz), 
                page.mediabox.top 
                )
            writer.add_page(page)
            with open(fname, "wb") as fp:
                writer.write(fp)


        if legend is not None:
            
            lname = os.path.join(self.saveloc, Path(filename + "_legend").with_suffix(".pdf"))
            legend.savefig(lname, dpi='figure', bbox_inches="tight")

        return

    
