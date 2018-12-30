# -*- coding: utf-8 -*-


import pytest

from src import examplelib


@pytest.fixture()
def library():
    return examplelib
