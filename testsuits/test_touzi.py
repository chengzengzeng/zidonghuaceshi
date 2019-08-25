#coding=utf-8
import unittest
from pageobjects.cut import *
from time import *
from framework.browser_engine import BrowserEngine
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class touzi(unittest.TestCase):

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

    #投资流程
    def test_touzi(self):
        self.driver=self.login('licw')
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[3]/a/div[2]/div[2]').click()  # 点击项目管理
        self.driver.find_element_by_xpath(
                     '//*[@id="projectall"]/div[12]/div/div[1]/ul/li[1]/ul/li[4]/a/div').click()  # 点击投资项目
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath(
            '//*[@id="ProjectCreditAddition--v25"]/table/tbody/tr[5]/td[1]/div/table/tbody/tr/td/a[1]').click()  # 点击立项申请按钮
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)

        # 立项申请表填写
        self.driver.find_element_by_xpath(
            '//*[@id="projectName"]').send_keys("自动化测试-投资1")  # 输入项目名称
        s1 = Select(self.driver.find_element_by_id('sonProTypeId'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="1"的项，二级分类选择投资
        s1 = Select(self.driver.find_element_by_id('productType'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="1"的项，选择券商资管计划
        self.driver.find_element_by_xpath(
            '//*[@id="projectDes"]').send_keys("项目描叙")  # 输入项目描叙
        self.driver.find_element_by_xpath(
            '//*[@id="tags"]').send_keys("发行人")  # 输入发行人
        self.driver.find_element_by_xpath(
            '//*[@id="shortName"]').send_keys("简称")  # 输入简称
        self.driver.find_element_by_xpath(
            '//*[@id="regstCapital"]').send_keys("资本")  # 输入资本
        self.driver.find_element_by_xpath(
            '//*[@id="establishDate"]').send_keys("2019-06-04")  # 输入成立日期
        s1 = Select(self.driver.find_element_by_id('area'))  # 实例化Select
        s1.select_by_value("5")  # 选择value="5"的项，选择省份为山西省
        s1 = Select(self.driver.find_element_by_id('city'))  # 实例化Select
        s1.select_by_value("48")  # 选择value="48"的项，太原市
        self.driver.find_element_by_xpath(
            '//*[@id="companyType"]').send_keys("公司类型")  # 输入公司类型
        s1 = Select(self.driver.find_element_by_id('city'))  # 实例化Select
        s1.select_by_value("48")  # 选择value="48"的项，太原市
        s1 = Select(self.driver.find_element_by_id('isListed'))  # 实例化Select
        s1.select_by_value("0")  # 选择value="0"的项，选择否
        s1 = Select(self.driver.find_element_by_id('industryName'))  # 实例化Select
        s1.select_by_value("0")  # 选择value="0"的项，选择城投
        s1 = Select(self.driver.find_element_by_id('lastRating'))  # 实例化Select
        s1.select_by_value("0")  # 选择value="1"的项，信用评级选择无
        self.driver.find_element_by_xpath(
            '//*[@id="tradeAcc"]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  #上传交易结构
        self.driver.find_element_by_xpath(
            '//*[@id="financingPeriod"]').send_keys("2")  # 输入融资期限
        self.driver.find_element_by_xpath(
            '//*[@id="financingAmount"]').send_keys("2")  # 输入投资金额
        # self.driver.find_element_by_xpath(
        #     '//*[@id="proAcc"]/div[1]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传立项附件
        self.driver.find_element_by_xpath('//*[@id="addTrustPj"]') # 点击确定按钮
        self.driver.find_element_by_xpath(
            '//*[@id="addinvestproject"]/div[18]/div[3]/div/button[1]/span').click()  # 立项成功，点击确定按钮
        sleep(5)
        self.driver.close()

        # 李晨维  拟稿人分发
        self.driver = self.login('licw')
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
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="shenheTzlx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意!"的选项
        self.driver.find_element_by_xpath(
            '//*[@id="shenheTzlx0--i6"]').send_keys("处理意见")  # 输入处理意见
        self.driver.find_element_by_xpath(
            '//*[@id="shenheTzlx0--i9"]/table/tbody/tr/td[2]/a/input').send_keys("E:\\aa.txt")  # 上传附件
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击子公司会签按钮
        sleep(2)
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//form[@id="v2"]//a[contains(text(),"选择")]').click()  # 点击选择按钮
        self.driver.find_element_by_xpath(
            '//*[@id="_lMultiSelectDialog"]/table/tbody/tr[4]/td[1]/div/div[1]/ul/li[1]/ul/li[1]/ul/li[3]/a/span[2]').double_click()  # 双击选择李国柱
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[24]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.close()

if __name__ == '__main__':
    unittest.main()