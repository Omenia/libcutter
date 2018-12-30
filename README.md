# libcutter

Bootstrap a new (or enhance existing) Robot Framework test library
by a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template
that automates the repetitive development tasks and in addition provides
carefully selected Python excellence to publish more excellence,
that preferably does its thing well after years.

Goals, much inspired by [hatch](https://github.com/ofek/hatch):

1. Enhance Python and Robot Framework dev practices, but without reinventing the wheel
2. Tackle worsening Python dependency challenges, but with already established tools
3. Run `make` for (a)tests, build and tryout, but can also run them one by one

Features:

- Handles `virtualenv`s automatically, no need to know all its (fine) internals
- Neither this should interfere with emerging alternatives - let us know issues
- Everything needed for linting, hinting, formatting - knowing Python better
- Besides Robot Framework, bundles `pytest` and friendly plugins for unit tests
- Caution: Work in progress for portability and READMEs are prone to improve :)

## Python 3 should be enough now

As of December 2018, the Robot Framework community consensus seems to be
that new tools and libraries can skip series 2 and target for Python >= 3.6.
Though, do not drop support for Python 2 just yet, if it already exists
as this likely does not, at least, ease up the rest who are on the way to 3.

While this template started on Python 2, and has not removed its specifics,
it is not guaranteed that the included Python packages plan to support
[Python 2 much longer](https://pythonclock.org/).

## Prerequisites

Install `cookiecutter` from [PyPI](https://pypi.org/project/cookiecutter/):

    pip install --upgrade cookiecutter

## Usage

Prompts the directory name, library name and the package information (for PyPI):

    cookiecutter .

## Example

[examplelib](https://github.com/Omenia/libcutter/tree/master/examplelib)
was generated using the defaults in `cookiecutter.json`.
