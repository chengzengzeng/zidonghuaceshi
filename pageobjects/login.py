#coding=utf-8
from PIL import Image
from collections import defaultdict
import pytesseract
from time import *
from framework.browser_engine import BrowserEngine

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
    region = (662,322, 740, 356)
    # 裁切图片
    image = image.crop(region)
    imgry=image.convert('L')
    table= get_bin_table(threshold=210)
    out=imgry.point(table,'1')
    out=cut_noise(out)
    text=pytesseract.image_to_string(out)
    exclude_char_list =' .,:\\|\'\"?![]（）()!@#$%^&*_+{};<>/¥'
    text = ''.join([x for x in text if x not in exclude_char_list])
    return text.replace('¥','y')

# 登录
def test_login(self):
    browser = BrowserEngine(self)
    self.driver = browser.open_browser(self)  # 读取浏览器类型
    while True:
        self.driver.find_element_by_name("userName").send_keys(lidl)  # 输入用户名
        sleep(1)
        self.driver.find_element_by_name("password").send_keys("1234")  # 输入密码
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