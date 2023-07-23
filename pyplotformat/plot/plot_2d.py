'''
Format class for 2D plots.
'''
from matplotlib import pyplot as plt

from .format import Format

class Format2D(Format):
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

    def __call__(self,
                figure : plt.Figure,
                **kwargs : dict
                ) -> tuple[plt.Figure, plt.Axes]:
        '''Format a 2D figure according to class attributes and specified or default parameters.

        Format a matplotlib 2D (cartesian axis) figure containing an axes object with data already 
        plotted. Returns the formatted plots. This method can be called using *Format2D()*.
        
        Parameters
        ----------
        figure : matplotlib.pyplot.Figure
            Matplotlib `Figure` object containing a single axes with data plotted.
        **kwargs : dict, optional
            Extra arguments that can be supplied to modify formatting. See :ref:'Other Parameters'
        
        .. _Other Parameters:
        Other Parameters
        ----------------
        xlabel : str, optional
            Label for the x-axis. (default value is None, will leave empty axis)
        ylabel : str, optional
            Label for the y-axis. (default value is None, will leave empty axis)
        title : str, optional
            Title of the plot. (default value is None, will leave empty title)
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
        lxpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the left edge of the line.
            (default value is 1.0) 
        uxpad : float, optional
            Multiplier for the extra whitespace inside of the axes from the left edge of the line.
            (default value is 1.0)
        lypad : float, optional
            Multiplier for the extra whitespace inside of the axes from the lowest point of the
            line. (default value is 1.1) 
        uypad : float, optional
            Multiplier for the extra whitespace inside of the axes from the highest point of the
            line. (default value is 1.1)
        xylim : list, optional
            If not None, this value overrides the default axis limits set by the padding variables.
            (default value is None)
        xscale : str, optional
            Scale for the x-axis using matplotlib settings. (default value is None)
        yscale : str, optional
            Scale for the y-axis using matplotlib settings. (default value is None)
        
        Returns
        -------
        figure : matplotlib.pyplot.Figure
            matplotlib `Figure` object with formatting applied.
        axes : matplotlib.plyplot.Axes
            matplotlib `Axes` object with formatting applied.
        '''


        kwargs = self._parse_input(figure, **kwargs)
        self._format_fig_size(**kwargs)
        self._format_axes_labels(**kwargs)
        self._format_ticks(**kwargs)
        self._format_line_colors(**kwargs)
        self._format_line_annotation(**kwargs)
        self._format_axes_limits(**kwargs)
        self._format_axes_scale(**kwargs)
        self._format_tight_layout(**kwargs)
        self._display(**kwargs)

        return self.figure, self.axes
