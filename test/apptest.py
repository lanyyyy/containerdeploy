#-*- coding: utf-8 -*-
#!/usr/bin/python
__author__ = 'lanyyyy'

import unittest
import os
from utils.ymlparser import YamlParser


class FuncTest(unittest.TestCase):

    def setUp(self):
        os.putenv("APPLICATION_ENV", "dev")

    def test_yaml(self):
        YamlParser("dev")
        self.assertNotEquals(YamlParser("dev").info, {})
        self.assertNotEquals(YamlParser("dev").info, None)

if __name__ == '__main__':
    unittest.main()
#     # 1、设置待执行用例的目录
#     test_dir = os.path.join(os.getcwd())
#
#     # 2、自动搜索指定目录下的cas，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
#     discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
#
#     # 实例化TextTestRunner类
#     runner = unittest.TextTestRunner()
#
#     # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
#     runner.run(discover)
