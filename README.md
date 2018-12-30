# libcutter

Bootstrap a new (or enhances the existing) Robot Framework test library
using a [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template,
to automate all the repetitive development tasks, but also to provide carefully
selected hinting tools to publish Python packages that surely work everywhere.

Goals:

1. Embrace Python and Robot Framework good practices, but without reinventing wheel
2. Tackle ever-worsening Python dependency issues, but with widely known tools
3. Run `make` for tests, build and publish, but can run also only stage as well

Features:

- Handles `virtualenv`s automatically, you avoiding complicated internals
- Neither should interfere with some emerging options - please report if issues
- Includes tools for linting, hinting, formatting and bettering your Python code
- In addition to Robot Framework, includes an enhanced pytest for unit testing
- Extensive testing is still work in progress - currently with <10 code bases

## Python 3 only is enough now

As of December 2018, the consencus in Robot Framework community is that
new tools and libraries can target to work on Python >= 3.6 only.

While this template was started on Python 2, it cannot be quaranteed the tools
included continue to support [Python 2 for a long](https://pythonclock.org/).

## Prerequisites

Install cookiecutter from [PyPI](https://pypi.org/project/cookiecutter/):

    pip install --upgrade cookiecutter

## Bootstrap a library

This asks the directory and package names and the info required by PyPI:

    cookiecutter .

The defaults are in `cookiecutter.json`.
