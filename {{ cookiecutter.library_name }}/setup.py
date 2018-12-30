#!/usr/bin/env python
# -*- coding: utf-8 -*-


from io import open  # required for Python 2
from os.path import abspath, dirname, join
from setuptools import find_packages, setup

classifiers = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: {{ cookiecutter.license }}
Operating System :: OS Independent
Programming Language :: Python :: 3 :: Only
Programming Language :: Python :: 3.6
Programming Language :: Python :: 3.7
Topic :: Software Development :: Testing
Framework :: Robot Framework
Framework :: Robot Framework :: Library
""".strip().splitlines()

curdir = dirname(abspath(__file__))
with open(join(curdir, "src", "{{ cookiecutter.library_name }}", "version.py"), encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.strip().split("=")[1].strip(" '\"")
            break
    else:
        version = "0.0.1"
with open(join(curdir, "README.md"), encoding="utf-8") as f:
    readme = f.read()
with open(join(curdir, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read()

setup(
    name="{{ cookiecutter.package_name }}",
    version=version,
    description="Robot Framework test library template",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="{{ cookiecutter.author_name }}",
    author_email="{{ cookiecutter.author_email }}",
    license="Apache License 2.0",
    url="{{ cookiecutter.url }}",
    platforms="console",
    keywords="{{ cookiecutter.package_keywords }}",
    classifiers=classifiers,
    install_requires=requirements,
    zip_safe=False,
    package_dir={"": "src"},
    packages=find_packages("src"),
)
