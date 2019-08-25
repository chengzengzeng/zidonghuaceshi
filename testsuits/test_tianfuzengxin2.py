#coding=utf-8
import unittest
from selenium import webdriver
from PIL import Image
from collections import defaultdict
import pytesseract
from time import *
from selenium.webdriver.support.ui import Select

def get_threshold(image):
    pixel_dict=defaultdict(int)
    rows,cols=image.size
    for i in range(rows):
        for j in range(cols):
            pixel = image.getpixel((i,j))
            pixel_dict[pixel]+=1
    count_max =max(pixel_dict.values())
    pixel_dict_reverse={v:k for k,v in pixel_dict.items()}
    threshold=pixel_dict_reverse[count_max]
    print('threshold',threshold)
    return  threshold


def cut_noise(image):
    rows,cols =image.size
    change_pos =[ ]
    for i in range(1,rows-1):
        for j in range(1,cols-1):
            pixel_set=[]
            for m in range(i-1,i+2):
                for n in range(j-1,j+2):
                    if image.getpixel((m,n))!=1:
                        pixel_set.append(image.getpixel((m,n)))
            if len(pixel_set)<=4:
                change_pos.append((i,j))
    for pos in change_pos:
        image.putpixel(pos,1)
    return image


def get_bin_table(threshold):
    table=[]
    for i in range(256):
        rate=0.2
        if threshold *(1-rate) <=i<= threshold*(1+rate):
            table.append(1)
        else:
            table.append(0)
    return table


def OCR_lmj(img_path):
    image=Image.open(img_path)
    region = (943,325, 1040, 360)
    # 裁切图片
    image = image.crop(region)
    imgry=image.convert('L')
    #imgry.show()#显示图片
    table= get_bin_table(threshold=210)
    out=imgry.point(table,'1')
    out=cut_noise(out)
    text=pytesseract.image_to_string(out)
    exclude_char_list =' .,:\\|\'\"?![]（）()!@#$%^&*_+{};<>/¥'
    text = ''.join([x for x in text if x not in exclude_char_list])
    return text.replace('¥','y')

class zengxin2(unittest.TestCase):

    def login(self,name):
        # 加启动配置
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        # 打开chrome浏览器
        self.driver = webdriver.Chrome(chrome_options=option)
        self.driver.get("http://10.99.6.13:8080/zzxypmf/")
        self.driver.maximize_window()#窗口最大化
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
                    self.driver.find_element_by_xpath("/html/body/div[2]/form[1]/div/ul/li[4]/a").click()
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
        return self.driver

    #增信流程
    def test_zengxin2(self):
        #谭海涛-立项申请
        self.driver=self.login('tanhaitao')
        self.driver.find_element_by_xpath(
            '//*[@id="homepage"]/div[1]/div[1]/ul/li[3]/a/div[2]/div[2]').click()  # 点击项目管理
        self.driver.find_element_by_xpath(
            '//*[@id="projectall"]/div[12]/div/div[1]/ul/li[1]/ul/li[2]/a/div').click()  # 点击增信项目
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        self.driver.find_element_by_xpath(
            '//*[@id="ProjectInvestment--v24"]/table/tbody/tr[5]/td[1]/div/table/tbody/tr/td/a[1]').click()  # 点击立项申请按钮
        all_window = self.driver.window_handles
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)

        # 立项申请表填写
        self.driver.find_element_by_xpath(
            '//*[@id="projectName"]').send_keys("自动化测试-增信项目3")  # 输入项目名称 自动化测试-增信项目4
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="sonProTypeId"]'))
        s1.select_by_value("3")  # 二级分类，选择产业类
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="addtionType"]'))
        s1.select_by_value("1")  # 增信类型，增信类型
        self.driver.find_element_by_xpath(
            '//*[@id="projectDes"]').send_keys("项目描叙B")  # 输入项目描叙
        self.driver.find_element_by_xpath(
            '//*[@id="tags"]').send_keys("发行人B")  # 输入发行人
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="area"]'))  # 实例化Select
        s1.select_by_value("2")  # 选择北京
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="city"]'))  # 实例化Select
        s1.select_by_value("33")  # 选择北京市
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="industryName"]'))  # 实例化Select
        s1.select_by_value("1")  # 选择房地产
        self.driver.find_element_by_xpath(
            '//*[@id="addTrustPj"]').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #----------------立项尽调阶段-----------------#
        # 谭海涛-提交立项申请
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 朱鹏程-业务部负责人审批
        self.driver = self.login('zhupengcheng')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 陈永杰-风控部负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击分派人员审核
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ltiExerName"]').send_keys("熊水军")  # 搜索熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lbtQuery"]').click()  # 点击查询按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导按钮
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 熊水军-合规风控审查
        self.driver = self.login('xiongshuijun')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 陈永杰-风控部负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 尹刚-风控部领导审批
        self.driver = self.login('yingang')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 李静-总经理审批
        self.driver = self.login('lijing')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 谭海涛-尽职调查
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 朱鹏程-业务部负责人审批
        self.driver = self.login('zhupengcheng')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #------------------合规风控阶段----------------------#
        # 陈永杰-风控部负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击分派审核人员按钮
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ltiExerName"]').send_keys("熊水军")  # 搜索熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lbtQuery"]').click()  # 点击查询按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导按钮
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 熊水军-合规风控审查
        self.driver = self.login('xiongshuijun')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 陈永杰-风控部负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 尹刚-风控部领导审批
        self.driver = self.login('yingang')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #李静-总经理审批
        self.driver = self.login('lijing')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #------------------决策会阶段------------------------
        #谭海涛-上会申请
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #杨钧洁-决策会流程分发
        self.driver = self.login('yangjunjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击提交增信评审会按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #杨钧洁-评审会意见汇总
        self.driver = self.login('yangjunjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击主任审批按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #李静-评审委员会主任审批
        self.driver = self.login('lijing')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #杨钧洁-评审会结论录入
        self.driver = self.login('yangjunjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

                # 蒋刚-董事长审批
        self.driver = self.login('jianggang')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #杨钧洁-增信过会信息录入
        self.driver = self.login('yangjunjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i6"]').send_keys("意见发表")  # 输入意见
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i1"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="同意"的项
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i2"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="评审会"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i3"]').send_keys("2019-08-29")  #输入过会时间
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i4"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value="仅增信"的项
        self.driver.find_element_by_xpath(
            '//*[@id="pingshenhuiZx0--i5"]').send_keys("2") #输入审批过会金额
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="pingshenhuiZx0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #--------------------合同阶段--------------------------#
        # 谭海涛-合同用印申请
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="ui-id-3"]').click()  # 点击项目合同
        self.driver.switch_to.frame("projectInfo--v2")  # 切换到框架中
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="project_contract_c"]/div/a').click()  # 点击发起合同流程
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="title"]').send_keys("测试标题")  # 输入申请标题
        self.driver.find_element_by_xpath(
            '//*[@id="zxbase.contractName"]').send_keys("增信函1")  # 输入增信函名称
        self.driver.find_element_by_xpath(
            '//*[@id="zzxyContractNo"]').send_keys("ZXHBH")  # 输入增信函编号
        self.driver.find_element_by_xpath(
            '//*[@id="zzxyLiabilityAmount"]').send_keys("1")  # 输入责任金额
        self.driver.find_element_by_xpath(
            '//*[@id="zxxyRate"]').send_keys("10")  # 输入费率
        self.driver.find_element_by_xpath(
            '//*[@id="releaseDeadline"]').send_keys("2")  # 输入发行期限
        self.driver.find_element_by_xpath(
            '//*[@id="save_input"]').click()  # 点击提交按钮
        sleep(5)
        self.driver.quit()

        # 谭海涛-合同办理
        self.driver = self.login('tanhaitao')
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
        sleep(5)
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
        self.driver.quit()

        # 朱鹏程-业务部门负责人审批
        self.driver = self.login('zhupengcheng')
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
        sleep(5)
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
        self.driver.quit()

        # 陈永杰-风控负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击分派审核人员按钮
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ltiExerName"]').send_keys("熊水军")  # 搜索熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lbtQuery"]').click()  # 点击查询按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导按钮
        self.driver.find_element_by_xpath(
            '//*[@id="projectpanoramaflowview"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 熊水军-合同审查
        self.driver = self.login('xiongshuijun')
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
        sleep(5)
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
        self.driver.quit()

        # 陈永杰-风控部门负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
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
        self.driver.quit()

        # 尹刚-风控部领导审批
        self.driver = self.login('yingang')
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
        sleep(5)
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
        self.driver.quit()

        # 李静-总经理审批
        self.driver = self.login('lijing')
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
        sleep(5)
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
        self.driver.quit()

        # 蒋刚-董事长审批
        self.driver = self.login('jianggang')
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
        sleep(5)
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
        self.driver.quit()

        # 谭海涛-通知用印
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击增信函用印按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 凌晓晨-增信函用印
        self.driver = self.login('lingxiaochen')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="LF20160708130824135_auditForm0--i7"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i1"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击增信函用印按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 合同签订-增信函上传
        self.driver = self.login('yangjunjie')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        self.driver.find_element_by_xpath(
            '//*[@id="LF20160708130824135_auditForm0--i3"]').send_keys("ZXHBH")  # 输入增信函编号
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
        self.driver.quit()

        #------------------------发行及放款---------------------------#
        # 谭海涛-合同用印申请
        self.driver = self.login('tanhaitao')
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
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ui-id-4"]').click()  # 点击发行及放款
        self.driver.switch_to.frame("projectInfo--v6")  # 切换到框架中
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="project_product_c"]/div[1]/a').click()  # 点击新增发行
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="productName"]').send_keys("发行名称")  # 输入发行名称
        self.driver.find_element_by_xpath(
            '//*[@id="issueDate"]').send_keys("2019-09-01")  # 输入发行时间
        self.driver.find_element_by_xpath(
            '//*[@id="issueScale"]').send_keys("1")  # 输入发行金额
        self.driver.find_element_by_xpath(
            '//*[@id="sf-submit"]').click()  # 点击提交审核按钮
        sleep(5)
        self.driver.quit()

        # 谭海涛-发行确认
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        self.driver.find_element_by_xpath(
            '//*[@id="lodldald"]').click()  # 点击快速审批按钮
        self.driver.switch_to.frame("projectInfo--v1")  # 切换到框架中
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.switch_to.default_content()  # 退出iframe的方法,回到了最外层的html页面
        self.driver.find_element_by_xpath(
            '//*[@id="projectinfo"]/div[20]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        #-----------------------跟踪管理阶段------------------------#
        # 谭海涛-待跟踪计划触发跟踪流程
        self.driver = self.login('tanhaitao')
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
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ui-id-8"]').click()  # 点击项目跟踪
        self.driver.switch_to.frame("projectInfo--v14")  # 切换到框架中
        # 先定义一下当前窗口句柄　
        first_window = self.driver.current_window_handle
        print(first_window)
        self.driver.find_element_by_xpath(
            '//*[@id="addProjectTrack"]').click()  # 点击添加跟踪按钮
        all_window = self.driver.window_handles
        print(all_window)
        for i in all_window:
            if i != first_window:
                self.driver.switch_to_window(i)
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="addTrackRecord--i5"]').send_keys("跟踪名称1")  # 输入跟踪名称
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="addTrackRecord--i27"]/select'))  # 实例化Select
        s1.select_by_value("1")  # 选择value=""的项 正常
        self.driver.find_element_by_xpath(
            '//*[@id="addTrackRecord--i19"]').send_keys("2019-07-02")  # 输入跟踪时间
        self.driver.find_element_by_xpath(
            '//*[@id="addTrackRecord--i28"]').send_keys("跟踪描叙")  # 输入跟踪描叙
        self.driver.find_element_by_xpath(
            '//*[@id="addTrackRecord--l_el_id_10"]').click()  # 点击提交审核按钮
        sleep(5)
        self.driver.quit()


        # 谭海涛-跟踪信息填写
        self.driver = self.login('tanhaitao')
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
        sleep(5)
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[18]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 朱鹏程-部门经理审批
        self.driver = self.login('zhupengcheng')
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
        sleep(5)
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[18]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 陈永杰-风控部门负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击分派人员审核按钮
        sleep(2)
        self.driver.find_element_by_xpath(
            '//*[@id="ltiExerName"]').send_keys("熊水军")  # 搜索熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lbtQuery"]').click()  # 点击查询按钮
        self.driver.find_element_by_xpath(
            '//*[@id="canExerSel"]/div[2]/table/tbody/tr/td[1]/label').click()  # 选中熊水军
        self.driver.find_element_by_xpath(
            '//*[@id="lMultiSelectDialogBtn1"]').click()  # 点击右导按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[14]/div[11]/div/button[1]/span').click()  # 点击确定按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[19]/div[3]/div/button[1]/span').click()  # 点击审核通过按钮
        sleep(5)
        self.driver.quit()


        # 熊水军-跟踪调查
        self.driver = self.login('xiongshuijun')
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
        sleep(5)
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[18]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()

        # 陈永杰-风控部门负责人审批
        self.driver = self.login('chenyongjie')
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
        sleep(5)
        s1 = Select(
            self.driver.find_element_by_xpath('//*[@id="commonAuditForm0--i5"]/select'))  # 实例化Select
        s1.select_by_value("同意！")  # 选择value="同意"的项
        self.driver.find_element_by_xpath(
            '//*[@id="commonAuditForm0--i2"]').send_keys("意见发表")  # 输入意见
        self.driver.find_element_by_xpath(
            '//*[@id="insButton_0"]').click()  # 点击通过按钮
        self.driver.find_element_by_xpath(
            '//*[@id="painsdetail2"]/div[18]/div[3]/div/button[1]/span').click()  # 点击确定按钮
        sleep(5)
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()