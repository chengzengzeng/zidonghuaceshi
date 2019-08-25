#coding=utf-8
import unittest
from pageobjects.cut import *
from logs.logger import Logger
from time import *
from framework.browser_engine import BrowserEngine



class shouye(unittest.TestCase):

    def setUp(self):
        browser = BrowserEngine(self)
        self.driver = browser.open_browser(self) # 读取浏览器类型

    # 登录
    def test_shouye(self):

        while True:
            self.driver.find_element_by_name("userName").send_keys("pmadmin")#输入用户名
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

        self.driver.maximize_window()

        #常用功能
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[1]/a/div').click()  # 点击待办
        # self.driver.find_element_by_xpath('//*[@id="SystemManage--i12"]').send_keys("请")
        # self.driver.find_element_by_xpath(
        #     '//*[@id="SystemManage--v8"]/table/tbody/tr[3]/td[7]/div/table/tbody/tr/td/a').click()  # 点击查询
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[2]/a/div').click()  # 点击预警
        self.driver.back()
        sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[3]/a/div').click()  # 点击任务管理
        # self.driver.back()
        # sleep(1)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[4]/a/div').click()  # 点击最新动态
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[5]/a/div').click()  # 点击项目周报
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[6]/a/div').click()  # 点击录入月度收入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[7]/a/div').click()  # 点击录入投资标的分布
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[8]/a/div').click()  # 点击录入非标投资行业分布
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[9]/a/div').click()  # 点击公司年度预算录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[10]/a/div').click()  # 点击首页资管规模录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[11]/a/div').click()  # 点击首页资管基金录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[12]/a/div').click()  # 点击首页个人增信录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[13]/a/div').click()  # 点击首页鹏元资信录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[14]/a/div').click()  # 点击信用云个人增信录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[15]/a/div').click()  # 点击新闻事件
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[16]/a/div').click()  # 点击信用云个人增信
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[17]/a/div').click()  # 点击中小微企业业务
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[18]/a/div').click()  # 点击个人增信项目详情
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[19]/a/div').click()  # 点击线上产品中小微
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[20]/a/div').click()  # 点击修改增信业务概况
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[21]/a/div').click()  # 点击修改中小微企业
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[22]/a/div').click()  # 点击修改线上中小微
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[1]/ul/li[23]/a/div').click()  # 点击信用云逾期率详表
        self.driver.back()
        sleep(2)

        #收藏
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[1]/a/div').click()  # 点击所有项目
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[2]/a/div').click()  # 点击增信项目
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[3]/a/div').click()  # 点击投资项目
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[4]/a/div').click()  # 点击资管项目
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[5]/a/div').click()  # 点击测试用
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[2]/ul/li[6]/a/div').click()  # 点击修改密码
        self.driver.back()
        sleep(2)

        #征信子公司
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[3]/ul/li[1]/a/div').click()  # 点击咨询项目维护
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[3]/ul/li[2]/a/div').click()  # 点击项目金额录入
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[3]/ul/li[3]/a/div').click()  # 点击数据资产信息维护
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[3]/ul/li[4]/a/div').click()  # 点击销售线索信息维护
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[13]/div/div[1]/ul/li[3]/ul/li[5]/a/div').click()  # 点击预鉴系统信息维护
        self.driver.back()
        sleep(2)

        # 顶部导航菜单
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[2]/a/div[2]/div[2]').click()  # 点击首页
        self.driver.back()
        sleep(2)
        # self.driver.find_element_by_xpath(
        #     '//*[@id="homepage"]/div[1]/div[1]/ul/li[3]/a/div[2]/div[2]').click()  # 点击数据支持
        # self.driver.back()
        # sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[4]/a/div[2]/div[2]').click()  # 点击项目管理
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[5]/a/div[2]/div[2]').click()  # 点击客户管理
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[6]/a/div[2]/div[2]').click()  # 点击统计报表
        self.driver.back()
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        # 显示当前的所有句柄(后面handle加s)
        all_window = self.driver.window_handles
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[8]/a/div[2]/div[2]').click()  # 点击知识库
        self.driver.back()
        sleep(5)
        # 返回到之前的窗口
        for i in all_window:
            if i == first_window:
                self.driver.switch_to.window(i)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[8]/a/div[2]/div[2]').click()  # 点击组织管理
        self.driver.back()
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[9]/a/div[2]/div[2]').click()  # 点击系统功能
        self.driver.back()
        sleep(2)


        #先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        #显示当前的所有句柄(后面handle加s)
        all_window = self.driver.window_handles
        #用一个判断进行切换，切换到弹出的窗口
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
                self.driver.find_element_by_xpath(
                    '//*[@id="warning"]/div[13]/div/div[1]/ul/li[1]/ul/li[2]/a/div').click()  # 点击预警
        #返回到之前的窗口
        for i in all_window:
            if i == first_window:
                self.driver.switch_to.window(i)


if __name__ == '__main__':
    unittest.main()

