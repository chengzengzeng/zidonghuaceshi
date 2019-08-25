#coding=utf-8
import unittest
from pageobjects.cut import *
from time import *
from framework.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import Select

class zengxin(unittest.TestCase):

    def login(self,name):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self)  # 读取浏览器类型
        while True:
            self.driver.find_element_by_name("userName").send_keys(name)#输入用户名
            sleep(1)
            self.driver.find_element_by_name("password").send_keys("1234")#输入密码
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

    #增信流程
    def test_zengxin(self):
        # self.driver=self.login('lidl')
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="homepage"]/div[1]/div[1]/ul/li[4]/a/div[2]/div[2]').click()  # 点击项目管理
        # # 显示当前的所有句柄(后面handle加s)
        # all_window = self.driver.window_handles
        # print(all_window)
        # # 用一个判断进行切换，切换到弹出的窗口
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        #     else:
        #         self.driver.find_element_by_xpath(
        #              '//*[@id="projectall"]/div[12]/div/div[1]/ul/li[1]/ul/li[2]/a/div').click()  # 点击增信（含担改投）
        # # 先定义一下当前窗口句柄　
        # first_window = self.driver.current_window_handle
        # print(first_window)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="ProjectInvestment--v24"]/table/tbody/tr[5]/td[1]/div/table/tbody/tr/td/a[1]').click()  # 点击立项申请按钮
        # all_window = self.driver.window_handles
        # print(all_window)
        # for i in all_window:
        #     if i != first_window:
        #         self.driver.switch_to_window(i)
        #         print(self.driver.title)
        #
        # #立项申请表填写
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectName"]').send_keys("自动化测试-增信1")  # 输入项目名称
        # s1 = Select(self.driver.find_element_by_id('sonProTypeId'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，二级分类
        # s1 = Select(self.driver.find_element_by_id('addtionType'))  # 实例化Select
        # s1.select_by_value("1")  # 选择value="1"的项，增信类型
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectDes"]').send_keys("项目描叙")  # 输入项目描叙
        # self.driver.find_element_by_xpath(
        #     '//*[@id="tags"]').send_keys("发行人")  # 输入发行人
        # s1 = Select(self.driver.find_element_by_id('area'))  # 实例化Select
        # s1.select_by_value("20")  # 选择value="1"的项，广东省
        # s1 = Select(self.driver.find_element_by_id('city'))  # 实例化Select
        # s1.select_by_value("232")  # 选择value="1"的项，广州市
        # s1 = Select(self.driver.find_element_by_id('industryName'))  # 实例化Select
        # s1.select_by_value("2")  # 选择value="1"的项，金融
        # s1 = Select(self.driver.find_element_by_id('lastRating'))  # 实例化Select
        # s1.select_by_value("0")  # 选择value="1"的项，无
        # self.driver.find_element_by_xpath(
        #     '//*[@id="addTrustPj"]').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # #李东来
        # self.driver=self.login('lidl')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击提交部门经理按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # #王冠
        # self.driver=self.login('wangguan')
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
        # self.driver.switch_to.frame("projectInfo--v1") #切换到框架中
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # #李东来
        # self.driver=self.login('lidl')
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
        # self.driver.switch_to.frame("projectInfo--v1") #切换到框架中
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # # 李东来
        # self.driver=self.login('lidl')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="jdAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # #杨越
        # self.driver=self.login('yangyue')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        #
        # #杨越
        # self.driver=self.login('yangyue')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()#退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #             '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        #
        # # 王冠
        # self.driver=self.login('wangguan')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # # 郎魏
        # self.driver=self.login('langwei')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # sleep(5)
        # self.driver.close()
        #
        # # 杨越
        # self.driver=self.login('yangyue')
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
        # # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # # s1.select_by_value("同意！")  # 选择value="同意"的项
        # self.driver.find_element_by_xpath(
        #     '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        # self.driver.find_element_by_xpath(
        #     '//*[@id="insButton_0"]').click()  # 点击通过按钮
        # self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        # self.driver.find_element_by_xpath(
        #     '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        # self.driver.close()

        # 陈国阳
        self.driver=self.login('chengy')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击指定人员审核按钮
        self.driver.find_element_by_xpath(
            '//*[@id="ltiExerName"]').send_keys("王洋")  # 搜索王洋
        self.driver.find_element_by_xpath(
            '//*[@id="lbtQuery"]').click()  # 点击查询按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中王洋
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 右边选中
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.close()

        # 王洋
        self.driver=self.login('wangyang')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 陈国洋
        self.driver=self.login('chengy')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_1"]').click()  # 点击通过按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 勾选牛冠兴
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导入
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 牛冠兴
        self.driver=self.login('niugx')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 杨彬
        self.driver=self.login('yangbin')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 李东来
        self.driver=self.login('lidl')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_1"]').click()  # 点击提交上会
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 杨彬
        self.driver=self.login('yangbin')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_1"]').click()  # 上评审会
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 杨彬
        self.driver=self.login('yangbin')
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
        # s1 = Select(self.driver.find_element_by_id('commonAuditForm0--i5'))  # 实例化Select
        # s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 杨彬
        self.driver=self.login('yangbin')
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
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i1"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="1"的项，通过
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i2"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="1"的项，评审会
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i3"]').send_keys("2019-06-03")  # 输入过会时间
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i4"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="1"的项，仅增信
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i5"]').send_keys("100")  # 输入过会时间
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意！"的项，同意
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        #---------------------合同阶段---------------------#
        # 李东来----合同用印申请
        self.driver=self.login('lidl')
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
            '//*[@id="ui-id-3"]').click()  # 点击项目合同
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        self.driver.switch_to.frame("projectInfo--v2")  # 切换到框架中
        self.driver.find_element_by_xpath(
            '//*[@id="project_contract_c"]/div/a').click()  # 点击发起合同流程
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                print(self.driver.title)
        self.driver.find_element_by_xpath(
            '//*[@id="title"]').send_keys("合同4")  #输入申请标题
        self.driver.find_element_by_xpath(
            '//*[@id="zxbase.contractName"]').send_keys("测试的合同4")  # 输入合同名称
        self.driver.find_element_by_xpath(
            '//*[@id="zzxyContractNo"]').send_keys("biaohao")  # 输入项目编号
        self.driver.find_element_by_xpath(
            '//*[@id="zzxyLiabilityAmount"]').send_keys("10")  # 输入责任金额
        self.driver.find_element_by_xpath(
            '//*[@id="zxxyRate"]').send_keys("10")  # 输入费率
        self.driver.find_element_by_xpath(
            '//*[@id="releaseDeadline"]').send_keys("1")  # 输入发行期限
        self.driver.find_element_by_xpath(
            '//*[@id="zxFile"]/div[2]/div[4]/div[1]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.png")
        sleep(2)
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="save_input"]').click()  # 点击提交按钮
        sleep(5)
        self.driver.quit()


        # 李东来----拟稿人分发
        self.driver=self.login('lidl')
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
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 提交部门经理
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()


        # 王冠----提交部门经理
        self.driver=self.login('wangguan')
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
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 杨越----质控岗复核
        self.driver=self.login('yangyue')
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
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击提交风控法务部
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 徐明明----风控法务部分发
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
            '//*[@id="insButton_0"]').click()  # 指定人员审核
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr[1]/td[1]/label').click()  # 点击选中框
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导入
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 王洋----合规风控审核
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
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 陈国阳----风控法务部总经理
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
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 李东来----项目组拟稿人
        self.driver = self.login('lidl')
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
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 郭贤达----资金财务部审批
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
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 李东来----项目组拟稿人
        self.driver = self.login('lidl')
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
            '//*[@id="insButton_0"]').click()  # 提交公司文秘
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 宋梅----公司综合文秘
        self.driver = self.login('songmei')
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
            '//*[@id="insButton_0"]').click()  # 提交公司文秘
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 宋梅----用印前确认
        self.driver = self.login('songmei')
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
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 李东来----项目经理
        self.driver = self.login('lidl')
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
            '//*[@id="insButton_0"]').click()  # 点击合同用印
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        # 刘偏偏----运营岗经办
        self.driver = self.login('liupp')
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
            '//*[@id="insButton_0"]').click()  # 点击结束用印
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

        #-----------------发行阶段---------------------#
        # 李东来----新增发行
        self.driver = self.login('lidl')
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
            '//*[@id="productName"]').send_keys("产品1")
        self.driver.find_element_by_xpath(
            '//*[@id="issueScale"]').send_keys("10")
        self.driver.find_element_by_xpath(
            '//*[@id="zstypeRateL"]/input').send_keys("20")
        self.driver.find_element_by_xpath(
            '//*[@id="zs-durationR"]/input[1]').send_keys("1")
        self.driver.find_element_by_xpath(
            '//*[@id="issueDate"]').send_keys("2019-06-04")
        self.driver.find_element_by_xpath(
            '//*[@id="valueDate"]').send_keys("2019-06-05")
        self.driver.find_element_by_xpath(
            '//*[@id="expirationDate"]').send_keys("2020-06-05")
        self.driver.find_element_by_xpath(
            '//*[@id="proAcc"]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.png") #上传文件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="projectchargeview"]/div[10]/div[4]/table[2]/tbody/tr[6]/td[2]/input[1]').click() #选择收费种类增信费
        self.driver.find_element_by_xpath(
            '//*[@id="zs-fchargingDate"]').send_keys("2019-06-04") #输入首次收费
        self.driver.find_element_by_xpath(
            '//*[@id="zs-div"]/table[1]/tbody/tr[6]/td/a[1]').click()  # 点击下载模板按钮
        sleep(5)
        self.driver.close()




if __name__ == '__main__':
    unittest.main()
