#coding=utf-8
import unittest
from pageobjects.cut import *
from time import *
from framework.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import Select

class ziguan(unittest.TestCase):

    def login(self,name):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)  # 读取浏览器类型
        while True:
            self.driver.find_element_by_name("userName").send_keys(name)#输入用户名
            sleep(1)
            self.driver.find_element_by_name("password").send_keys("Csci20170301?")#输入密码
            sleep(1)
            while True:
                self.driver.get_screenshot_as_file('E:\\aa.png')  # 截图
                sleep(1)
                yzm = OCR_lmj('E:\\aa.png')  # 截取验证码部门的图片
                if len(yzm) == 4:  # 判断验证码的位数是否为4位
                    break
                    print(yzm)
                else:
                    self.driver.find_element_by_xpath("/html/body/div/div[2]/form[1]/div/ul/li[4]/a").click()
            print(yzm)
            self.driver.find_element_by_name("rand").send_keys(yzm)#输入验证码
            sleep(1)
            self.driver.find_element_by_class_name('login_bt').click()#点击登录按钮
            try:
                text_field = self.driver.find_element_by_id('errorId').is_displayed()  # 判断红色提示文字是否显示
                print(text_field)
                if text_field == False:
                    sleep(1)
                    break
            except:
                print("登录成功")
                sleep(1)
                break
        self.driver.maximize_window()#窗口最大化
        return self.driver

    #资管流程
    def test_ziguan(self):
        # self.driver=self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="homepage"]/div[1]/div[1]/ul/li[4]/a/div[2]/div[1]').click()  # 点击项目管理
        #
        # self.driver.find_element_by_xpath(
        #              '//*[@id="projectall"]/div[12]/div/div[1]/ul/li[1]/ul/li[5]/a/div').click()  # 点击资管项目
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="ProjectAsset--v22"]/table/tbody/tr[5]/td[1]/div/table/tbody/tr/td/a[1]').click()  # 点击立项申请按钮
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #
        # #立项申请表填写
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectName"]').send_keys("自动化测试-资管1")  # 输入项目名称
        # s1 = Select(self.driver.find_element_by_id('sonProTypeId'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，二级分类
        # s1 = Select(self.driver.find_element_by_id('zgType'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，项目类型
        # s1 = Select(self.driver.find_element_by_id('productType'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，产品类型
        # s1 = Select(self.driver.find_element_by_id('coopType'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，合作机构类型
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectDes"]').send_keys("项目描叙")  # 输入项目描叙
        # self.driver.find_element_by_xpath(
        #     '//*[@id="tags"]').send_keys("融资主体")  # 输入融资主体
        # s1 = Select(self.driver.find_element_by_id('area'))  # 实例化Select
        # s1.select_by_value("20")  # 选择value="1"的项，广东省
        # s1 = Select(self.driver.find_element_by_id('city'))  # 实例化Select
        # s1.select_by_value("232")  # 选择value="1"的项，广州市
        # s1 = Select(self.driver.find_element_by_id('industryName'))  # 实例化Select
        # s1.select_by_value("2")  # 选择value="1"的项，金融行业
        # s1 = Select(self.driver.find_element_by_id('lastRating'))  # 实例化Select
        # s1.select_by_value("0")  # 选择value="1"的项，无
        # self.driver.find_element_by_xpath(
        #     '//*[@id="tradeAcc"]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传交易结构
        # sleep(5)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="addInfoManage"]').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # #宋大龙
        # self.driver=self.login('songdl')
        # #先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1") #切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="jdAuditForm0--i8"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陆蔚
        # self.driver = self.login('luwei')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="jdAuditForm0--i8"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 明建华
        # self.driver = self.login('mingjh')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="jdAuditForm0--i8"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="jdAuditForm0--i8"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="jdAuditForm0--i8"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 刘鑫
        # self.driver = self.login('liuxin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="shenheZgs0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 刘鑫
        # self.driver = self.login('liuxin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="shenheZgs0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 明建华
        # self.driver = self.login('mingjh')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="shenheZgs0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="shenheZgs0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="shenheZgs0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击报母公司按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陈国阳
        # self.driver = self.login('chengy')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击指定人员审核
        # self.driver.find_element_by_xpath(
        #     '//*[@id="canExerSel"]/div[2]/table/tbody/tr[1]/td[1]/label').click()  # 勾选王洋
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导入按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 王洋
        # self.driver = self.login('wangyang')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陈国阳
        # self.driver = self.login('chengy')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过【选择执行人】按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中公司领导牛冠兴
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导入按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 牛冠兴
        # self.driver = self.login('niugx')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 杨彬
        # self.driver = self.login('yangbin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i3"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_1"]').click()  # 点击提交风控法务部
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陈国阳
        # self.driver = self.login('chengy')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击指定人员审核按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="canExerSel"]/div[2]/table/tbody/tr[1]/td[1]/label').click()  # 选择王洋
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导入按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 王洋
        # self.driver = self.login('wangyang')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陈国阳
        # self.driver = self.login('chengy')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_1"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()

        # # 宋梅
        # self.driver = self.login('songmei')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_1"]').click()  # 点击上评审会按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()

        # # 杨彬
        # self.driver = self.login('yangbin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 杨彬
        # self.driver = self.login('yangbin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i1"]/select'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="通过"的项
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i2"]/select'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="评审会"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i3"]').send_keys("2019-06-12")  # 输入过会时间
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i4"]/select'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="仅增信"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i5"]').send_keys("200")  # 输入审批过会金额
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZg0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i6"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="pingshenhuiZg0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # #-------------------合同阶段------------------------
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projects-zs-table"]/tbody/tr[2]/td[1]/a').click()  # 点击该项目
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="ui-id-3"]').click()  # 点击项目合同
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # self.driver.switch_to.frame("projectInfo--v2")  # 切换到框架中
        # self.driver.find_element_by_xpath(
        #     '//*[@id="project_contract_c"]/div/a').click()  # 点击发起合同流程
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="title"]').send_keys("合同1")  # 输入申请标题
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpContractName"]').send_keys("测试的合同1")  # 输入合同名称
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpContractNo"]').send_keys("biaohao")  # 输入项目编号
        # self.driver.find_element_by_xpath(
        #     '//*[@id="gl.productName"]').send_keys("产品名称")  # 输入产品名称
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpOutsourcingFee"]').send_keys("10")  # 输入外包费
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpTimeLimit"]').send_keys("1")  # 输入期限
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpManagementFee"]').send_keys("10")  # 输入管理费
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zgcpManagedClassesFee"]').send_keys("10")  # 输入托管费
        # self.driver.find_element_by_xpath(
        #     '//*[@id="NoFenJInput"]').send_keys("10")  # 输入产品份额
        # self.driver.find_element_by_xpath(
        #     '//*[@id="glFile"]/div[2]/div[4]/div[1]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.png")
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="save_input"]').click()  # 点击提交按钮
        # sleep(2)
        # self.driver.quit()

        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击发起子公司会签按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(
        #     self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
        #     "E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_1"]').click()  # 点击提交综合风控部按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 刘鑫
        # self.driver = self.login('liuxin')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(
        #     self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
        #     "E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 陆蔚
        # self.driver = self.login('luwei')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(
        #     self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
        #     "E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()
        #
        # # 宋大龙
        # self.driver = self.login('songdl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        # self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        # s1 = Select(
        #     self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
        #     "E:\\aa.txt")  # 上传附件
        # sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_1"]').click()  # 选择子公司章报母公司
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(2)
        # self.driver.close()

        # 徐明明
        self.driver = self.login('xumm')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 选择指定人员审核
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr[1]/td[1]/label').click()  # 选择王洋
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 选择右导如按钮
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 宋大龙
        self.driver = self.login('wangyang')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 选择通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 陈国阳
        self.driver = self.login('chengy')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 选择通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 宋大龙
        self.driver = self.login('songdl')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 选择通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 郭贤达
        self.driver = self.login('guoxd')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 选择通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 宋大龙
        self.driver = self.login('songdl')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击转资金财务部审批按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 郭贤达
        self.driver = self.login('guoxd')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 宋大龙
        self.driver = self.login('songdl')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_1"]').click()  # 提交子公司总经理
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 明建华
        self.driver = self.login('mingjh')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 宋大龙
        self.driver = self.login('songdl')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击合同用印按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 齐心陪
        self.driver = self.login('qixp')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        # 刘伟
        self.driver = self.login('liuwei')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="messageInfo"]/div[1]').click()  # 点击第一个待办
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i2"]/table/tbody/tr/td[2]/a/input').send_keys(
            "E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(2)
        self.driver.close()

        #----------------------发行阶段-----------------------------
        # 宋大龙----新增发行
        self.driver = self.login('songdl')
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="projects-zs-table"]/tbody/tr[2]/td[1]/a').click()  # 点击该项目
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ui-id-4"]').click()  # 点击产品及收费
        self.driver.switch_to.frame("projectInfo--v6")  # 切换到框架中
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath(
            '//*[@id="project_product_c"]/div[1]/a').click()  # 点击新增发行
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="productName"]').send_keys("产品1") #输入产品名称
        self.driver.find_element_by_xpath(
            '//*[@id="issueScale"]').send_keys("10") #输入发行金额
        self.driver.find_element_by_xpath(
            '//*[@id="zstypeRateL"]/input').send_keys("20") #输入年利率
        self.driver.find_element_by_xpath(
            '//*[@id="zs-durationR"]/input[1]').send_keys("1") #输入发行期限
        self.driver.find_element_by_xpath(
            '//*[@id="issueDate"]').send_keys("2019-06-04") #输入发行日期
        self.driver.find_element_by_xpath(
            '//*[@id="valueDate"]').send_keys("2019-06-05") #输入起息日
        self.driver.find_element_by_xpath(
            '//*[@id="expirationDate"]').send_keys("2020-06-05") #输入到期日
        self.driver.find_element_by_xpath(
            '//*[@id="proAcc"]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.png")  # 上传文件
        self.driver.find_element_by_xpath(
            '//*[@id="projectchargeview"]/div[10]/div[4]/table[2]/tbody/tr[7]/td[2]/input[3]').click()  # 选择收费种类管理费
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="gl-fchargingDate"]').send_keys("2019-06-04") #输入首次收费
        self.driver.find_element_by_xpath(
            '//*[@id="gl-div"]/table[1]/tbody/tr[5]/td/a[1]').click()  # 点击下载模板按钮
        # self.driver.find_element_by_xpath(
        #     '//*[@id="zs-div"]/table[1]/tbody/tr[6]/td/a[2]').send_keys("E:\\12_20190604143532_收费计划.xls")
        # self.driver.find_element_by_xpath(
        #     '//*[@id="sf-submit"]').click()  # 点击提交审核
        sleep(2)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()