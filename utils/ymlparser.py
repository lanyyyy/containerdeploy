#-*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'lanyyyy'

import os
import yaml
import sys


class YamlParser():

    def __init__(self, env):
        self.confdir = os.path.join(os.path.split(os.path.dirname(__file__))[0], "config")
        self.yamlfile = os.path.join(self.confdir, self.get_conffiles(env))
        self.info = self.get_app_conf()

    def get_conffiles(self, env):
        yamlfile = ""
        if env == "dev":
            yamlfile = "application-dev.yaml"
        elif env == "prod":
            yamlfile = "application-prod.yaml"
        if yamlfile == "":
            print "Get Wrong conf, env is none"
            sys.exit(1)
        return yamlfile

    def get_app_conf(self):
        """
            根据不同的参数解析配置
            @:param env:   dev：application-dev.yaml
                            prod：application-prod.yaml
                            others：暂不考虑其他扩展
        """
        data = {}
        with open(self.yamlfile, "r+") as fd:
            data = yaml.load(fd)
        return data

# TODO: 这里临时将环境设为“dev”
os.environ["APPLICATION_ENV"] = "dev"
env = os.environ["APPLICATION_ENV"]
CONF = YamlParser(env).info


