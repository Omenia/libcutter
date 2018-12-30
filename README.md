# libcutter

Bootstrap a new (or enhance existing) Robot Framework test library
by a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template
that automates the repetitive development tasks and in addition provides
carefully selected Python excellence to publish more excellence,
that surely works anywhere.

Goals:

1. Enhance Python and Robot Framework dev practices, but without reinventing wheel
2. Tackle ever-worsening Python dependency issues, but with widely known tools
3. Run `make` for tests, build and publish, but can also run one of them as well

Features:

- Handles `virtualenv`s automatically, no need to learn complicated internals
- Neither it should interfere with emerging alternatives - please report issues
- Everything needed for linting, hinting, formatting and bettering Python code
- In addition to Robot Framework, includes an enhanced pytest for unit testing
- Caution: Extensive testing work in progress, also READMEs prone to improve :)

## Python 3 should be enough now

As of December 2018, the consencus in Robot Framework community seems to be
that new tools and libraries can forget 2 series and target for Python >= 3.6.

While this template was started on Python 2, and still seems to work on it,
it cannot be quaranteed if íncluded tools want to support
[Python 2 how long](https://pythonclock.org/).

## Prerequisites

Install cookiecutter from [PyPI](https://pypi.org/project/cookiecutter/):

    pip install --upgrade cookiecutter

## Usage

Asks the directory, package name and other information required for PyPI:

    cookiecutter .

## Example

[examplelib](https://github.com/Omenia/libcutter/tree/master/examplelib)
is generated using the defaults in `cookiecutter.json`.
