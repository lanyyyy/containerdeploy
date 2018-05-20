#-*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'lanyyyy'

from utils.ymlparser import *


class TitanAuth(object):

    @classmethod
    def get_sign(cls):
        sign = ""
        if os.environ["TITAN_TEAM_NAME"] == u"精兵营":
            sign = CONF["titan"]["sign"]["jingbingying"]
        elif os.environ["TITAN_TEAM_NAME"] == u"伏羲":
            sign = CONF["titan"]["sign"]["fuxi"]
        return sign
