import pickle
from matplotlib import pyplot as plt
from pathlib import Path
from typing import Tuple

def saveFigure(filename: str, figure: plt.Figure, axes: plt.Axes) -> None:

    pickle.dump((figure, axes), open(Path(filename).with_suffix(".fig"), "wb"))
    return

def loadFigure(filename) -> Tuple[plt.Figure, plt.Axes]:

    return pickle.load( open(Path(filename).with_suffix(".fig"), "rb") )
