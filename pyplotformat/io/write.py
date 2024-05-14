'''
Utilities to produce image files from matplotlib figure objects.
'''

import os
from pathlib import Path
from matplotlib import pyplot as plt


def write_pdf(  figure : plt.Figure,
                filepath : str,
            ) -> None:
    '''Write formatted figure objects directly to PDF files.
    
    Write matplotlib `Figure` and `Axes` objects to .pdf files.

    Parameters
    ----------
    figure : matplotlib.pyplot.Figure
        Matplotlib `Figure` object containing a single axes with data plotted.
    filepath : str
        Name of the file for the figure .pdf. Extension is not required.
    '''

    fname = Path(filepath).with_suffix(".pdf")

    figure.savefig(fname, dpi='figure', bbox_inches="tight")


def write_svg(  figure : plt.Figure,
                filepath : str,
            ) -> None:
    '''Write formatted figure objects directly to SVG files.
    
    Write matplotlib `Figure` and `Axes` objects to .svg files.

    Parameters
    ----------
    figure : matplotlib.pyplot.Figure
        Matplotlib `Figure` object containing a single axes with data plotted.
    filepath : str
        Name of the file for the figure .svg. Extension is not required.
    '''

    fname = Path(filepath).with_suffix(".svg")

    figure.savefig(fname, dpi='figure', bbox_inches="tight")
