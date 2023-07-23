'''
This module contains the base class for formatting figure legends.
'''

#==================================================================================================
#
# #TODO: Need to work out number of legend columns required based on
#        width required of legend and using the wrap method to fix
#        the width of each legend entry.
#
#==================================================================================================

from matplotlib import pyplot as plt

from .default_values import _default_format_opts


class FormatLegend():
    '''This class contains the methods required to create and format matplotlib legends
    based on single or multiple fiugre inputs.

    Attributes
    ----------
    axes : list
        List of matplotlib.pyplot.Axes object in figures.
    lines : list
        List of matplotlib.pyplot.Line2D objects in figures.
    labels : list
        List of text labels associated with each line.
    SMALL_SIZE : float
        Size for small font text, equals 0.8*fontsize.
    MEDIUM_SIZE : float
        Size for standard plot text, equals fontsize.
    LARGE_SIZE : float
        Size fot large plot text, equals 1.2*fontsize.
    defaultfont : Dict
        Matplotlib kwargs dict for font. Describes default font family and size.
    figlegend : matplotlib.pyplot.Figure
        Figure object that contains the legend
    default_format_opts : Dict
        Default options for kwargs not provided to __call__().

    Parameters
    ----------
    max_width : str, {single, double}
        Maximum width the legend should take up before wrapping. Options are 'single'
        or 'double'. defaults to 'single'
    fontsize : float, optional
        Legend fontsize in pt. Defaults to 10
    '''
    # pylint: disable=too-many-instance-attributes
    # pylint: disable=too-few-public-methods

    def __init__(self, max_width="single", fontsize=10) -> None:

        self.axes = []
        self.lines = []
        self.labels = []

        self.width = max_width

        self.small_size = fontsize*0.8
        self.medium_size = fontsize
        self.bigger_size = fontsize*1.2

        self.defaultfont = {"family":   "Times New Roman",
                            "size":     self.medium_size,
                            }

        self.figlegend = plt.figure(figsize=(3.14961, 3.14961))

        self.default_format_opts = _default_format_opts


    def __call__(self, *figures, **kwargs) -> plt.Figure:
        '''Generate a legend for a set of figures.

        Generate a legend for a single figure or set of figures for all labelled lines
        plotted. Returns the formatted legend. This method can be called using *FormatLegend()*.
        
        Parameters
        ----------
        *figure : matplotlib.pyplot.Figure
            One or more Matplotlib `Figure` object each containing a single axes with data plotted.
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
        figlegend : matplotlib.pyplot.Figure
            matplotlib `Figure` object containing legend with formatting applied.
        '''

        kwargs = self._parse_input(**kwargs)
        self._assign_lines(*figures, **kwargs)
        self._format_legend(**kwargs)

        return self.figlegend


    def _parse_input(self,
                    **kwargs) -> dict:

        # Parse optional arguments or assign default values
        for key, value in self.default_format_opts.items():
            if key not in kwargs:
                kwargs[key] = value

        return kwargs

    def _assign_lines(self, *figures, **kwargs):

        # Concatenate all axes objects together
        for fig in figures:
            self.axes += fig.get_axes()

        # Get all lines in all axes
        for axes in self.axes:
            self.lines += axes.get_lines()

        # Get label for each line
        for line in self.lines:
            self.labels.append(line._label)


    def _format_legend(self, **kwargs):

        if kwargs['annotate']:
            
            raise NotImplementedError("Generating legends for annotated plots is not yet\
                                       implemented.")

            '''
            NOTE: Below is the old code for handling annotated legends. This will need to be
                  updated for this class, along with some method of dealing with multiple figure
                  inputs where the annotate property is different for both.

            obj = []
            legend_map = {}
            for line, slab in zip(axes.get_lines(), shortlabel):
                obj.append( TextLegend(slab, line.get_color()) )
            for o in obj:
                legend_map[o] = TextLegendHandler()
        
            leg = figlegend.legend(obj, label, handler_map=legend_map, prop=self.legendfont, 
                                   loc="center", ncol=ncol)
            leg.get_frame().set_edgecolor("black")
            figlegend.tight_layout()
            '''
        else:
            leg = self.figlegend.legend(self.lines, self.labels, prop=self.defaultfont,
                                        loc="center", ncol=4)


        leg.get_frame().set_edgecolor("black")
        for axes in self.figlegend.axes:
            axes.remove()
        self.figlegend.tight_layout()
