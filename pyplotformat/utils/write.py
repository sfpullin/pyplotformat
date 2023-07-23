'''
Utilities to produce image files from matplotlib figure objects.
'''

import os
from pathlib import Path
from matplotlib import pyplot as plt


def write_pdf(   figure : plt.Figure,
                saveloc : str,
                filename : str,
            ) -> None:
    '''Write formatted figure objects directly to separate PDF files.
    
    Write matplotlib `Figure` and `Axes` objects to .pdf files including an optional
    legend parameter if one is creeated as a separate figure object. The file save
    location will depend on the `saveloc` attribute supplied to this class on creation
    and the string provided to this method as a parameter.

    Parameters
    ----------
    figure : matplotlib.pyplot.Figure
        Matplotlib `Figure` object containing a single axes with data plotted.
    filename : str
        Name of the file for the figure .pdf. Extension is not required.
    '''

    fname = os.path.join(saveloc, Path(filename).with_suffix(".pdf"))

    figure.savefig(fname, dpi='figure', bbox_inches="tight")



# NOTE: Some tool to visualize and 'move' a group of pdf figs and legend(s)
#       then generate one PDF of the final image would be useful.
