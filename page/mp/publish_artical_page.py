"发布文章界面"
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base.mp_base.base_page import BasePage, BaseHandle

# 对象库层
from utils import DriverUtils, check_channel_option


class PubAriPage(BasePage):
    # 使用实例属性定义所有要操作的元素定位方式以及表达式
    # 使用实例方法找所有要用到的元素对象
    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, "[placeholder='文章名称']")
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, "#publishTinymce_ifr")
        # 内容
        self.ari_context = (By.CSS_SELECTOR, "body")
        # 封面
        self.ari_cover = (By.XPATH, "//*[text()='自动']")
        # 频道选择框
        self.channel = (By.CSS_SELECTOR, "[placeholder='请选择']")
        # 频道选项
        self.channel_option = (By.XPATH, "//*[text()='android']")
        # 发表
        self.pub_btn = (By.XPATH, "//*[text()='发表']")

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找 iframe
    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    # 找封面
    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    # 找频道选择框
    def find_channel(self):
        return self.find_elt(self.channel)

    # 找频道选择项
    def find_channel_option(self):
        return self.find_elt(self.channel_option)

    # 找发表按钮
    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层
class PubAriHandle(BaseHandle):

    def __init__(self):
        self.pub_ari_page = PubAriPage()

    # 文章标题的输入
    def input_ari_title(self, title):
        self.input_text(self.pub_ari_page.find_ari_title(), title)

    # 文章内容的输入
    def input_ari_content(self, context):
        # iframe 切换
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_ari_page.find_ari_iframe())
        # 输入文章的内容 #
        self.input_text(self.pub_ari_page.find_ari_context(), context)
        # 返回默认界面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def check_ari_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    # 选择频道
    def check_ari_channel(self, channel_name):
        # 调用工具类中的公用下拉框选择方法
        check_channel_option(DriverUtils.get_mp_driver(), "请选择", channel_name)

    # 发表点击
    def click_pub_ari_btn(self):
        self.pub_ari_page.find_pub_btn().click()


# 业务层
class PubAriProxy:

    def __init__(self):
        self.pub_ari_handle = PubAriHandle()

    # 发布文章的业务方法
    def test_pub_aritcal(self, title, context, channel_name):
        # 2.输入标题
        self.pub_ari_handle.input_ari_title(title)
        # 3.输入内容
        self.pub_ari_handle.input_ari_content(context)
        # 4.选择封面
        self.pub_ari_handle.check_ari_cover()
        # 5.选择频道
        self.pub_ari_handle.check_ari_channel(channel_name)
        # 6.点击发表按钮
        self.pub_ari_handle.click_pub_ari_btn()
