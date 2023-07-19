# pyPlotFormat
## Version 0.0.6
Tool for fast and consistent plot generation with the Matplotlib library.

## About
This tool aims to apply constistent formatting in the creation of data visualisation methods generated through the matplotlib library in Python. It also aims to speed up the process of producing publishable-quality figures by directly producing PDF images that can be inserted into documents. Importantly, the PDF figures generated by this tool are limited to 3 sizes (W x H):

- 'single' - 8cm x 7cm
- 'double' - 16cm x 7cm
- 'large' - 16cm x 14cm

The width's that are used here are designed to fit on an A4 page with 1in margins, which is standard for many manuscript formats (including AIAA). Either two adjecent 'single' figures or one 'double' or 'large' figure will align with the text. Figure legends can be produced as a separate PDF file and combined with the corresponding figure at the word processing or document markup stage.

When including the PDF figures in a document rescaling should be avoided as the text size is predefined by the formatter. By default the format uses 10pt text, though this can be set as desired.

## Installation
First clone the repository using,

```shell
git clone https://github.com/sfpullin/plotter.git
```

Then move into the cloned directory and install using ```pip```:

```shell
pip install .
```

## Quickstart

### Formattting a 2D plot
Before formatting a plot, one must be created through the matplotlib library. As an example we can create a simple graph of ```y = sin(x)``` and then return a ```Figure``` and ```Axes``` matplotlib object using the ```matplotlib.pyplot.subplots()```python funciton:

```python
import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(0.0, 4*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()
ax.plot(x,y)
```

The formatting of this figure is then handled with the Format class provided in the corresponding plotting module. In this case:

```python
from pyplotformat.plot.plot2D import Format as Format2D

f2D = format2D(shape="single", fonsize=10)
```

This creates a format object ```f2D``` and specifies that the figure should be a 'single' size (8cm x 7cm) and the font size should be 10pt. (Note these are the default values of thes input variables, but are included here as an example) 

The figure created earlier can then be formatted by supplying the ```Figure``` and ```Axes``` object to the ```Format``` object:

```python
fig, ax, leg = f2D(fig, ax, xlabel="x", ylabel="y",
                    label=["sin(x)"], separatelegend=True, annotate=True, shortlabel=["Y1"])
```

The above line passes the ```Figure``` and ```Axes``` object to be formatted. Additionally we specify a label for the x and y axis, give the line a label, put the legend in a separate plot and annotate the created line with a short label placed outside the right y-axis of the plot. The returned values are the newly formatted ```Figure``` and ```Axes``` matplotlib objects, as well as a separate legend ```Figure```.

To produce the PDF of these figures the write method of the ```Format``` class can be used:

```python
f2D.write("example", fig, ax, leg)
```

This will create a PDF of both the figure, named "example.pdf" and the legend, named "example_legend.pdf". These can then be directly included in a document through a word processing or document markup software.

### Saving a figure
It is also possible to save a figure for later formatting or modification if required. This can be achived through the utils module. Assuming that a matplotlib ```Figure``` and ```Axes``` objects have been created, named ```fig``` and ```ax``` respectively, the figure can be saved using,

```python
from pyplotformat import utils as putils

putlis.saveFigure("example", fig, ax)
```

This will save the figure as "example.fig" in the working directory (note this is not compatible with the MATLAB .fig format). The figure file can then be loaded when required:

```python
from pyplotformat import utils as putils

fig, ax = putlis.loadFigure("example.fig")
```

The figure can then be reformatted and saved.

## Reference documentaion

**To be completed**
