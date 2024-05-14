'''
Format class for polar plots.
'''
from matplotlib import pyplot as plt
import matplotlib.ticker as mticker

from .format import Format
from .default_values import _default_polar_format_opts

from math import pi
import numpy as np

class FormatPolar(Format):
    '''Format object which contains methods for formatting and writing matplotlib figures

    This class can be initialised with global parameters that will affect the entire figure.
    The created class can then be used to format multiple figures with these parameters.

    Parameters
    ----------
    shape : str, optional
        Figure shape as it should appear in a document. Options are 'single', 'double' and 'large',
        which correspond to 8cm x 7cm, 16cm x 7cm and 16cm x 14cm respectively. These sizes should
        take up half or all of the text width of a A4 document with 1" margins. (default value is 
        'single')
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
    # pylint: disable=too-few-public-methods
    # Only need the __call__ method for this class
    # May add other set_ and get_ methods at a later date

    def __init__(self,
                 shape : str = "single",
                 fontsize : int = 10,
                 saveloc : str = ".") -> None:

        super().__init__(shape, fontsize, saveloc)
        self.default_format_opts = _default_polar_format_opts

    def __call__(self,
                figure : plt.Figure,
                **kwargs : dict
                ) -> tuple[plt.Figure, plt.Axes]:
        '''Format a polar figure according to class attributes and specified or default parameters.

        Format a matplotlib 2D (cartesian axis) figure containing an axes object with data already 
        plotted. Returns the formatted plots. This method can be called using *FormatPolar()*.
        
        Parameters
        ----------
        figure : matplotlib.pyplot.Figure
            Matplotlib `Figure` object containing a single axes with data plotted.
        **kwargs : dict, optional
            Extra arguments that can be supplied to modify formatting. See :ref:'Other Parameters'
        
        .. _Other Parameters:
        Other Parameters
        ----------------
        tlabel : str, optional
            Label for the x-axis. (default value is None, will leave empty axis)
        rlabel : str, optional
            Label for the y-axis. (default value is None, will leave empty axis)
        title : str, optional
            Title of the plot. (default value is None, will leave empty title)
        axis_shape: str, optional
            Shape of the polar axis. Options are full, for full 360 degree plot, half for a 0 
            to 180 deg plot and quart for a 0 to 90 deg plot. Deafult is full.
        orient : str, optional
            Direction of theta axis, either counterclockwise 'CCW' or clockwise 'CW'. Default is 'CCW'.
        zero_location : str, optional
            Position of the zero angle on the screen in compass orientation. Default is 'E'
        show : bool, optional
            If `True` will show the plot before it is returned using `matplotlib.pyplot.show()`
        color : list, optional
            List of colors defined by strings (either matplotlib aliases or hex codes) with a 
            length equal to the number of lines. This can be used to override the default color
            scheme. A subset of lines can keep the default color scheme by leaving the 
            corresponding list position with a value of `None`. (default value is `None`, which
            uses default color scheme)
        shortlabel : list, optional
            List of strings that can be placed at the rightmost edge of each line to help define
            it. This label will replace the legend handle. Useful for plots that do not use color
            to distinguish between lines. Labels should be between 1 and 3 characters. (default 
            value is None)
        annotate : bool, optional
            If `True` this option will enable short labels placed at the rightmost edge of each
            line to help define it. If `False` short labels will not be used. (default `False`)
        blackline : bool, optional
            If `True` all lines will be coloured black. If `False` the default colour scheme will
            be used (or those specified by the color parameter). (default value is `False`)
        rlim : list, optional
            Limits of the radial axis of the plot. Default None
        lrpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the lowest point of the
            line. (default value is 1.1) 
        urpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the highest point of the
            line. (default value is 1.1)
        rscale : str, optional
            Scale for the r-axis using matplotlib settings. (default value is None)
        
        Returns
        -------
        figure : matplotlib.pyplot.Figure
            matplotlib `Figure` object with formatting applied.
        axes : matplotlib.plyplot.Axes
            matplotlib `Axes` object with formatting applied.
        '''
        

        kwargs = self._parse_input(figure, **kwargs)
        self._format_polar_options(**kwargs)
        self._format_fig_size(**kwargs)
        self._format_axes_limits(**kwargs)
        self._format_ticks(**kwargs)
        self._format_axes_labels(**kwargs)
        self._format_line_colors(**kwargs)
        self._format_line_annotation(**kwargs)
        self._format_axes_scale(**kwargs)
        self._format_tight_layout(**kwargs)
        self._display(**kwargs)

        return self.figure, self.axes


    def _format_polar_options(self,
                                **kwargs):

        if self.axes.name != "polar":

            raise("Axis type ", self.figure.axes[0].name, "is not supported for polar formatter.\
                    To enable polar format, use: plt.subplots(subplot_kw={'projection': 'polar'})")

        
        if kwargs['axis_shape'] == 'full':
            tmax = 360
        elif kwargs['axis_shape'] == 'half':  
            tmax = 180
        elif kwargs['axis_shape'] == 'quart':
            tmax = 90
        else:
            Warning("Argument for axis_shape \'" + kwargs['axis_shape'] + "\', unrecognized, \
                    defaulting to \'full\'")
            tmax = 360
        

        self.axes.set_thetamin(0)
        self.axes.set_thetamax(tmax)


        if kwargs['orient'] == "CW":
            self.axes.set_theta_direction(-1)
        

        self.axes.set_theta_zero_location(kwargs['zero_location'])

    
    def _format_axes_labels(self,
                          **kwargs):

        # Set label and titles
        # =========================================================================================
        if kwargs['tlabel'] is not None:
            self.axes.set_xlabel(kwargs['tlabel'], **self.axesfont)
        if kwargs['rlabel'] is not None:
            
            rax_mid_point = self.axes.get_rmin() + (self.axes.get_rmax() - self.axes.get_rmin())/2

            if kwargs['axis_shape'] == 'full':
                label_position=self.axes.get_rlabel_position()
                self.axes.text(np.radians(label_position-10),rax_mid_point,kwargs['rlabel'],
                rotation=label_position,ha='center',va='center', **self.axesfont)
            else:
                self.axes.text(np.radians(-35),rax_mid_point,kwargs['rlabel'],
                rotation=0.0,ha='center',va='center', **self.axesfont)

            #self.axes.set_ylabel(kwargs['rlabel'], **self.axesfont)
        if kwargs['title'] is not None:
            self.axes.set_suptitle(kwargs['title'], **self.titlefont)


    def _format_ticks(self,
                        **kwargs):

        # Set tick formatting
        # =========================================================================================
        ticks_loc = self.axes.get_xticks().tolist()
        self.axes.xaxis.set_major_locator(mticker.FixedLocator(ticks_loc))

        ticks_loc = self.axes.get_yticks()
        self.axes.yaxis.set_major_locator(mticker.FixedLocator(ticks_loc))

        self.axes.set_xticklabels(["{:.5g}°".format(tick*180/pi) for tick in self.axes.get_xticks()]\
                                , **self.tickfont)
        self.axes.set_yticklabels(self.axes.get_yticks(), **self.tickfont)
        self.axes.yaxis.set_major_formatter('{x:.5g}')


        ticks_loc = self.axes.get_yticks()
        
        for tick in ticks_loc:
            self.axes.text(np.radians(0.0), tick, '{:.5g}'.format(tick),
                rotation=0.0,ha='center',va='top', **self.axesfont)

        self.axes.set_yticklabels([], **self.tickfont)

        self.axes.grid(linestyle=":", linewidth=0.7)
    

    def _format_axes_limits(self,
                          **kwargs):

        # Set axis limits
        # =========================================================================================

        if kwargs['rlim'] is None:
            rmin = 1e20
            rmax = 1e-20
            ymin = 1e20
            ymax = -1e20
            for line in self.axes.get_lines():
                # Remove None data for comparison
                y_data = [y for y in line.get_ydata() if y is not None]
                if min(y_data) < ymin:
                    ymin = min(y_data)
                if max(y_data) > ymax:
                    ymax = max(y_data)


            self.axes.set_ylim(kwargs['lypad']*ymin, kwargs['uypad']*ymax)
        else:
            self.axes.set_ylim(kwargs['rlim'][0], kwargs['rlim'][1])
                
