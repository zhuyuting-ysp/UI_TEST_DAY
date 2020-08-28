import json
import time

import allure
import selenium.webdriver
import appium.webdriver
import logging
# 定义浏览器驱动的工具类-自定义
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait


class DriverUtils:
    # 自媒体驱动对象私有属性
    __mp_driver = None
    # 后台管理系统
    __mis_driver = None
    # APP
    __app_driver = None

    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mp_driver = selenium.webdriver.Chrome()
            cls.__mp_driver.maximize_window()  # 窗口最大化
            cls.__mp_driver.implicitly_wait(30)  # 隐式等待
            cls.__mp_driver.get("http://ttmp.research.itcast.cn/")
        return cls.__mp_driver

    # mp 关闭浏览器的开关
    __mp_key = True

    # 自媒体-关闭浏览器驱动的方法
    @classmethod
    def quit_mp_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mp_driver is not None and cls.__mp_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mp_driver.quit()
            # 将__driver设置为空
            cls.__mp_driver = None

    # 修改mp自媒体关闭浏览器驱动的开关的方法
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 后台管理系统获取驱动对象得方法
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            # 创建浏览器驱动对象 --> 打开浏览器
            cls.__mis_driver = selenium.webdriver.Chrome()
            cls.__mis_driver.maximize_window()  # 窗口最大化
            cls.__mis_driver.implicitly_wait(30)  # 隐式等待
            cls.__mis_driver.get("http://ttmis.research.itcast.cn/")
        return cls.__mis_driver

    # 后台管理系统关闭驱动对象开关
    __mis_key = True

    # 修改后台管理系统驱动开关的方法
    @classmethod
    def change_mis_key(self, key):
        self.__mis_key = key

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_mis_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__mis_driver is not None and cls.__mis_key:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__mis_driver.quit()
            # 将__driver设置为空
            cls.__mis_driver = None

    # app系统获取驱动对象得方法
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '7.1.2'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__app_driver.implicitly_wait(30)
        return cls.__app_driver

    # 后台管理系统-关闭浏览器驱动的方法
    @classmethod
    def quit_app_driver(cls):
        # 为了保障代码的健壮性,防止异常报错,先判断当前是否有浏览器驱动对象是否存在
        if cls.__app_driver is not None:
            # 关闭浏览器
            time.sleep(4)
            # quit()只是关闭整个浏览器但是并不会将__driver的值设置为空,而是保留一串缓存字符串
            cls.__app_driver.quit()
            # 将__driver设置为空
            cls.__app_driver = None


# 根据文本判断元素是否存在的公用方法
def is_element_exist(driver, text):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(text(),'{}')]".format(text)
    # 显示等待查找元素，如果能找到元素则返回元素对象，找不到返回False,并且抛出异常
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到文本为{}的元素对象".format(text))

# 二次封装显示等待
def my_wait(driver,str_xpath):
    try:
        element = WebDriverWait(driver,10,0.5).until(lambda x:x.find_element_by_xpath(str_xpath))
        return element
    except Exception as e:
        NoSuchElementException("找不到{}的元素对象".format(str_xpath))

# 根据文本判断元素是否存在的公用方法
# def is_element_exist(driver, text):
def is_el_by_attribute(driver, attr_name,attr_value):
    # 定位元素的xpath表达式
    str_xpath = "//*[contains(@{},'{}')]".format(attr_name,attr_value)
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        NoSuchElementException("找不到属性={}且其值为{}的元素对象".format(attr_name,attr_value))
        return False


# 公用的下拉框选择方法
def check_channel_option(driver, channel_name, option_name):
    # 选择框的定位xpath表达式
    str_xpath = "//*[contains(@placeholder,'{}')]".format(channel_name)
    # 1.点击选择框的元素对象
    driver.find_element_by_xpath(str_xpath).click()

    # 2.选择频道框选项并点击
    # self.pub_ari_page.find_channel_option().click()
    # 2.获取所有选项的频道名称
    channel_option = driver.find_elements_by_css_selector(".el-select-dropdown__item span")
    # 默认定义一个是否找到的标识，默认为False
    is_suc = False

    # 3.对获取的的频道名称进行遍历
    for option_element in channel_option:
        # 4.判断当前遍历的元素文本信息是否等于我们所想选择的频道名称
        if option_element.text == option_name:
            # 如果则点击，跳出，并且把默认标识改Ture
            option_element.click()
            is_suc = True
            break
        # 如果不相等，鼠标悬浮到当前遍历的元素对象上并按下向下的按键
        else:
            # 创建鼠标对象
            action = ActionChains(driver)
            action.move_to_element(option_element).send_keys(Keys.DOWN).perform()
        # 默认标识始终是False
        # is_suc = False

    # 判断标识是否任为False，则跑出没找到对应的频道的选项
    if is_suc is False:
        NoSuchElementException("cann't find name is {} channel option".format(channel_name))


# 封装读取数据并组装成parameteriz 所要求数据格式函数
def get_case_data(file_path):
    # 定义一个空列表
    test_data = []
    # 1.读取数据文件中的数据
    with open(file=file_path, encoding="utf-8")as f:
        str_dict = json.load(f)
        # 2.遍历所有的键值
        for i in str_dict.values():
            # 3.一次性获取键值所有键值，并且把返回的结果直接追加到空列表中
            test_data.append(list(i.values()))
            print(test_data)

    return test_data

# allure截图公用方法
def get_allure_png(driver,filename):
    allure.attach(driver.get_screenshot_as_png(),filename,allure.attachment_type.PNG)