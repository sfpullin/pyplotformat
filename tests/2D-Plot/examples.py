from pyplotformat.plot import Format2D
from pyplotformat.plot import FormatLegend
from pyplotformat import io as putils

from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 100)

y1 = 1.2*np.sin(x)
y2 = np.sin(3*x + 0.3)

fig, ax = plt.subplots()

ax.plot(x, y1, label="data1")
ax.plot(x, y2, "--", label="data2")

fplot = Format2D()
lplot = FormatLegend()

fig, ax = fplot(fig, xlabel="x axis", ylabel="y axis")
leg = lplot(fig)

putils.writePDF(fig, ".", "example")
putils.writePDF(leg, ".", "example_legend")