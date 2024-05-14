# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.0] - 2024-05-15

### Added
- Support for inkscape integration. Calling the `inkscape()` function with a list of figures will directly open those figures as pdfs in inkscape.

### Changed
- Modified the repository structure to make use easier.

### Fixed
- `FormatLegend` no longer requires an `ncol` argument (default = 1).

## [0.2.1] - 2023-09-08

### Added

- Gridlines are now included on 2D plots by default. To turn off set `grid=False` to the formatting options.
- Option to specify tick locations on 2D plots with the `x_tick_loc` and `y_tick_loc` arguments.

### Fixed

- Fixed an issue that lead to no label being produced for the r-axis on polar plots

### Changed

- Default colors will now display in order for curves with None value colours even if colours are defined for other curves

## [0.2.0] - 2023-09-07

### Added

- Added functionality for polar plots to be formatted using the new `plot.FormatPolar` class.
- Added test script for polar plot formatter.

### Changed

- Changed .gitignore to ignore .vscode directories.

## [0.1.3] - 2023-08-22

### Fixed

- Fixed a bug that generated long high precision axis tick labels leading to distorted plots.

## [0.1.2] - 2023-08-04

### Fixed

- Fixed an issue that occured when formatting a 2D plot containing a line with a None type value.

## [0.1.1] - 2023-07-23

### Added

- Pylint configuration file `.pylintrc` added.

### Changed

- Formatting changes in most files to increase pylint score.

## [0.1.0] - 2023-07-23

### Added

- Opening this changelog.
- New `Format` class in `plot/format.py` forms the base class for any formatting methods. This class does not contain a `__call__` overload as this should be done in child classes.
- Added default methods to the `Format` class based on the 2D formatting methods. These can be individually overrided by children class types.
- Added a new `FormatLegend` class that handles legend creation from a single, or multiple figures.
- Added a new module, `utils/write.py`, which will contain functions for writing figures and legends to images.
- Added a `default_values.py` module which contains default values for use in plotting modules.

### Changed

- `plot/plot2D.py` now has new class `Format2D` which is a child of the new `Format` class.
- Package version is now defined only in top level `__init__.py` file.

### Removed

- Removed compatability for a combined plot and legend. Legends produced separately must be combined in the document formatting stage.
- Class method `write` in the `Format` class has been removed. Writing will now be handled by functions in the new `utils/write.py` module. 