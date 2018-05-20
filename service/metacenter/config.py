#-*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'lanyyyy'

import requests
from utils.ymlparser import *


class MetaCenter(object):

    def __init__(self):
        pass

    def get_image_tag(self, service, size=1, pagenum=1):
        """ 获取最新的镜像tag , 如果环境中有透传，则忽视
        """
        headers = {"Authoration": CONF["metacenter"]["authorization"]}
        uri = "?%s&size=%s?pageNum=%s" % (service, size, pagenum)
        requrl = CONF["metacenter"]["url"] + "/" + uri
        r = requests.post(requrl, headers=headers)

        for i in r["data"]["image"]:
            if i["type"] == "image":
                return i["tag"]
        return None
