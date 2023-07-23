# Changelog

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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