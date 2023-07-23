'''
Utilities to save and load figures through the use of Pickle. These figures
can then be reformatted at a later date.
'''

import pickle
from pathlib import Path
from matplotlib import pyplot as plt

def save_figure(filename: str, figure: plt.Figure, axes: plt.Axes) -> None:
    '''Save a figure for later use or formatting.
    
    Save a figure to a .fig extension. This figure contains the line data and
    formatting data of the plot. Resulting figure can be loaded later with 
    `loadFigure()`.

    Parameters
    ----------
    filename : str
        Name of the file to write to. Does not require an extension.
    figure : matplotlib.pyplot.Figure
        Matplotlib `Figure` object to be saved.
    axes : matplotlib.pyplot.Axes
        Matplotlig `Axes` object to be saved.
    '''
    with open(Path(filename).with_suffix(".fig"), "wb") as out_file:
        pickle.dump((figure, axes), out_file)

def load_figure(filename) -> tuple[plt.Figure, plt.Axes]:
    '''Load a saved figure for formatting and printing.

    Load a figure from a previously saved figure generated with the `saveFigure()`
    function. **WARNING**: The save method uses `pickle` to save files. The `pickle`
    method is not secure. Only load files from trusted sources!

    Parameters
    ----------
    filename : str
        Name of the .fig file to be loaded.

    Warning
    -------
    The save method uses `pickle` to save files. The `pickle` method is not secure
    and files can be maliciously altered to run code. Only load files from trusted sources!
    More details can be found at https://docs.python.org/3/library/pickle.html.
    
    Returns
    -------
    figure : matplotlib.pyplot.Figure
        Saved `Figure` object
    axes : matplotlib.pyplot.Axes
        Saved `Axes` object
    '''
    return pickle.load( open(Path(filename).with_suffix(".fig"), "rb") )
