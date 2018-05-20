# -*- coding: utf-8 -*-
# !/usr/bin/python
__author__ = 'lanyyyy'

import requests
from service.metacenter.config import MetaCenter
from utils.ymlparser import *
from titanauth import TitanAuth

DEPLOY_APPLY = {
    "app_name": "leapp",
    "INST_NAME": "demo-service-instance",
    "team_name": u"精兵营",
    "components": [{
        "service": "demo-service-cidbuild",
        "tag": "",
        "envs": ""  # 环境变量
    }]
}


def get_env(key):
    value = os.environ[key]
    print "get environment: %s=%s" % (key, value)
    if value == "":
        print "[WARNING] %s is null value" % key
    return value


class TitanDeploy(object):
    def __init__(self):
        pass

    def do_upgrade(self):
        body = self.set_upgrade_body()
        sign = TitanAuth.get_sign()
        if not sign:
            raise Exception("Not Get sign")
        headers = {"Context-type": "application/json", "Sign": sign}
        try:
            requests.post(CONF["titan"], headers=headers, body=body)
        except Exception, e:
            print "upgrade Failed"
            print e
            sys.exit(1)
        print "Upgrade Success"

    def set_upgrade_body(self):
        body = DEPLOY_APPLY
        body["app_name"] = get_env("TITAN_APP_NAME")
        body["inst_name"] = get_env("TITAN_INST_NAME")
        body["team_name"] = get_env("TITAN_TEAM_NAME")
        body["components"][0]["service"] = get_env("TITAN_SERVICE")
        body["components"][0]["envs"] = self.get_envs()
        body["componnets"][0]["tag"] = self.get_latest_imagetag()
        return body

    def get_envs(self):
        envs = get_env("ENVS")  # TODO 后续根据实际方式修改，应当从变量中透传
        return envs

    def get_latest_imagetag(self):
        """ 如果获取的镜像为空，那么直接从元数据中心获取镜像数据
        """
        imagetag = get_env("IMAGE_TAG")
        if not imagetag:
            meta = MetaCenter()
            imagetag = meta.get_image_tag(get_env("FUXI_SERVICE"))  # TODO：需要传入service参数，这里暂定为ENV：FUXI_SERVICE
        if not imagetag:
            raise Exception("Not Found imagetag")
        return imagetag
