def login(self, name):
    browser = BrowserEngine(self)
    self.driver = browser.open_browser(self)  # 读取浏览器类型
    while True:
        self.driver.find_element_by_name("userName").send_keys(name)  # 输入用户名
        sleep(1)
        self.driver.find_element_by_name("password").send_keys("Csci20170301?")  # 输入密码
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
        self.driver.find_element_by_name("rand").send_keys(yzm)  # 输入验证码
        sleep(1)
        self.driver.find_element_by_class_name('login_bt').click()  # 点击登录按钮
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

    self.driver.maximize_window()  # 窗口最大化
    return self.driver


