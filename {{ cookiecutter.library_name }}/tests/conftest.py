# -*- coding: utf-8 -*-


import pytest

from src import {{ cookiecutter.library_name }}


@pytest.fixture()
def library():
    return {{ cookiecutter.library_name }}
