from plotting.plot2D import Format

from matplotlib import pyplot as plt
import numpy as np

x = np.linspace(0.0, 10.0, 100)

y1 = 1.2*np.sin(x)
y2 = np.sin(3*x + 0.3)

fig, ax = plt.subplots()

ax.plot(x, y1)
ax.plot(x, y2)

fplot = Format()

fig, ax = fplot(fig, ax, "x axis", "y axis", label=["set 1", "set 2"])

fplot.write("example", fig, ax)