# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2023-09-15

Added tests for the core functionality of the package. Refactor some code to make it more testable.

### Added

- Tests for the core functionality of the package.
- A conda-forge recipe to build the package for conda.

### Changed

- Made the channels parameter of the segmentation widget modifiable from the UI.
- Refactored the main widget by pulling the update_layer function out of the main widget fuction. Instead it is a standalone function that is called by the main widget function.
- Improved the reader documentation.

### Removed

- Deleted the test for the full widget end to end in the UI. This test was better served in pieces of unit tests for individual functions.

## [0.04] - 2023-08-22

Updated package metadata for display on the napari hub.

## [0.0.3] - 2023-06-09

Improved the upload of the package to PyPI via GitHub actions.

## [0.0.2] - 2023-08-22

Initial release. Generated from the napari cookiecutter template.
napari hub and napari installer menu visibility have then been disabled after template generation.

### Added

- Initial segmentation of images in a widget.
- Created GitHub actions to run tests and build the package then upload to PyPI.
- Created an MkDocs documentation site. This site is updated via GitHub actions when a new release is made.
- Created a reader for NumPy files.
- Inlcuded sample data in the package of a calcium imaging file.
- First batch of tests for the package.

[1.0.0]: https://github.com/seankmartin/napari-software-development-workshop/releases/tag/v1.0.0
[0.0.4]: https://github.com/seankmartin/napari-software-development-workshop/releases/tag/v0.0.4
[0.0.3]: https://github.com/seankmartin/napari-software-development-workshop/releases/tag/v0.0.3
[0.0.2]: https://github.com/seankmartin/napari-software-development-workshop/releases/tag/v0.0.2