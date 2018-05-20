#!/usr/bin/python
# -*- coding: <encoding name> -*-

from service.titan.deploy import *
from utils.ymlparser import *
import argparse

parser = argparse.ArgumentParser("add")
parser.add_argument("-m", "method")
args = parser.parse_args()


def upgrade():
    m = TitanDeploy()
    pass


def main():
    # conf = configparser()
    print CONF
    if args.m == "upgrade":
        deploy = TitanDeploy()
        deploy.do_upgrade()


if __name__ == "__main__":
    main()
    pass
