# -*- coding: utf-8 -*-


import sys

from loguru import logger

from .keywords import Keywords
from .version import __version__


class examplelib(Keywords):

    # Not necessary in this case as 'TEST SUITE' is the default
    ROBOT_LIBRARY_SCOPE = "TEST SUITE"

    @logger.catch()
    def __init__(self):
        logger.add(sys.stderr, colorize=True)
        logger.trace(__version__)
