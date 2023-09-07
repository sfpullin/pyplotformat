from pyplotformat.plot import FormatPolar
from pyplotformat.plot import FormatLegend
from pyplotformat import utils as putils

from matplotlib import pyplot as plt
import numpy as np


def polar_func(th):

    return np.sin(th)


th = np.linspace(0.0, np.pi, 100)

r = polar_func(th)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

ax.plot(th, r)

plotFormat = FormatPolar()

fig, ax = plotFormat(fig, rlabel="SPL [dB]", axis_shape="half")

putils.write_pdf(fig, ".", "example")