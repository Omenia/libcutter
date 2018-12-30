# -*- coding: utf-8 -*-


from robot.api import logger
from robot.api.deco import keyword


class Keywords(object):
    def get_keyword_names(self):
        return [
            name
            for name in dir(self)
            if hasattr(getattr(self, name), "robot_name")
        ]

    @keyword
    def hello(self, who, *args, **kwargs):
        logger.console("\nHello %s" % (who))
