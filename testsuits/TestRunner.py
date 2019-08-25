# !/usr/bin/python
# -*- coding:utf-8 -*-

import unittest
import os
import time
from testsuits.test_get_page_title import GetPageTitle
from testsuits.baidu_search import BaiduSearch
from unit.HTMLTestRunner import HTMLTestRunner
# from testsuits.test_zengxin import zengxin
# from testsuits.test_ziguan import ziguan
from testsuits.test_tianfuzengxin1 import zengxin1
from testsuits.test_tianfuzengxin2 import zengxin2
from testsuits.test_tianfuzengxin3 import zengxin3
from testsuits.test_tianfutouzi1 import touzi1



# unittest suite 批量添加测试用例，逐个进行执行
suite = unittest.TestSuite()
suite.addTest(zengxin1('test_zengxin1'))
suite.addTest(zengxin2('test_zengxin2'))
suite.addTest(zengxin3('test_zengxin3'))
suite.addTest(touzi1('test_touzi1'))

# 添加一个类文件下的所有测试用例
# suite = []
# suite1 = unittest.TestSuite(unittest.makeSuite(BaiduSearch))
# suite2 = unittest.TestSuite(unittest.makeSuite(GetPageTitle))
# suite.append(suite1)
# suite.append(suite2)
# 如果添加多个测试类文件，那么将变量对象设置为数组，然后添加到数组中，最后进行循环遍历

# 测试报告 title
xxx_title = u"项目管理平台测试报告"
# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + "测试报告" + "HTMLtemplate.html"
print(HtmlFile)
isExists = os.path.exists(report_path)
if not isExists:
    try:
        os.makedirs(report_path)
    except Exception as e:
        print("创建文件夹失败",e)

if __name__ == '__main__':
    # open(HemlFile) 创建 html 测试报告
    with open(HtmlFile,"wb") as report:
        runner = HTMLTestRunner(stream=report,title=xxx_title,description=u"测试结果")
        runner.run(suite)
    # print(suite)
    # for i in suite:
    #     print(i)
    #     runner.run(i)

