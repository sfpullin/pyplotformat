import os
from matplotlib import pyplot as plt
import matplotlib
from pathlib import Path
from typing import Tuple
import pickle

from .textlegend import TextLegend, TextLegendHandler

_default_colors = [ '#1f78b4', '#33a02c', '#e31a1c',
                    '#ff7f00', '#6a3d9a', '#b15928',
                    '#a6cee3', '#b2df8a', '#fb9a99', 
                    '#fdbf6f', '#cab2d6', '#ffff99'
                    ]


#TODO: Eventually need a main class with all basic functions then create 
#       new classes that can deal with different plot types (polar, etc.)

class Format():

    def __init__(   self, 
                    shape="single", 
                    fontsize=10,
                    saveloc="."
                ) -> None:
        

        self.shape      = shape
        self.saveloc    = saveloc
        self.fontsize   = fontsize
        
            
        SMALL_SIZE = fontsize*0.8
        MEDIUM_SIZE = fontsize
        BIGGER_SIZE = fontsize*1.2

        self.defaultfont = {"family":   "Times New Roman",
                            "size":     MEDIUM_SIZE,
                            }
        
        self.axesfont = dict(self.defaultfont)

        self.titlefont = dict(self.defaultfont)
        self.titlefont['size'] = BIGGER_SIZE

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
                    annotate : bool = False,
                    blackline : bool = False,
                    lxpad : float = 1.0,
                    uxpad : float = 1.0,
                    lypad : float = 1.1,
                    uypad : float = 1.1,
                ) -> Tuple[plt.Figure, plt.Axes]:

        # Set figsize
        # ====================================================================================================
        if self.shape == "single":
            if label is not None:
                figure.set_size_inches(5.51181, 3.14961) # 10cm x 8cm
            else:
                figure.set_size_inches(3.14961, 3.14961) # 8cm x 8cm
        elif self.shape == "double":
            if label is not None:
                figure.set_size_inches(7.87402, 3.14961) # 20cm x 8cm
            else:
                figure.set_size_inches(6.29921, 3.14961) # 20cm x 8cm
        elif self.shape == "large":
            if label is not None:
                figure.set_size_inches(7.87402, 6.29921) # 20cm x 16cm
            else:
                figure.set_size_inches(6.29921, 6.29921) # 16cm x 16cm
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
            for line, name in zip(axes.get_lines, shortlabel):
                y = line.get_ydata()[-1]
                axes.annotate(name, xy=(1,y), xytext=(6,0), color=line.get_color(),
                                xycoords=axes.get_yaxis_transform(), textcoords="offset points",
                                size = 10, va="center")

        # Set line labels
        # ====================================================================================================
        if label is not None:
            for line, name in zip(axes.get_lines(), label):
                line.set_label(name)
        
        # Modify legend to include line labels
        # ====================================================================================================
        if annotate:
            obj = []
            legend_map = {}
            for line, slab in zip(axes.get_lines(), shortlabel):
                obj.append( TextLegend(slab, line.get_color()) )
            for o in obj:
                legend_map[o] = TextLegendHandler()

            leg = axes.legend(obj, handler_map=legend_map, prop=self.legendfont, loc="upper right")

        else:
            if label is not None:
                leg = axes.legend(prop=self.legendfont, loc="center left", bbox_to_anchor=(1, 0.5, 1.5748,0))
                leg.get_frame().set_edgecolor("black")


 
        # Set axis limits
        # ====================================================================================================

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

        # Set tight layout
        # ====================================================================================================
        figure.tight_layout()

        if show:
            plt.show()

        return figure, axes

    def write(   self,
                filename : str,
                figure : plt.Figure,
                axes : plt.Axes
            ) -> None:

        plt.savefig(os.path.join(self.saveloc, Path(filename).with_suffix(".pdf")), dpi='figure', bbox_inches="tight")

        return

    
