"首页"
from selenium.webdriver.common.by import By
from base.mp_base.base_page import BasePage, BaseHandle


# 对象库层
class HomePage(BasePage):

    def __init__(self):
        super().__init__()
        # 内容管理菜单
        self.context_tab = (By.XPATH, "//*[text()='内容管理']")
        # 发布文章导航栏
        self.pub_ari_tab = (By.XPATH, "//*[contains(text(),'发布文章')]")

    # 找到内容管理菜单
    def find_context_tab(self):
        return self.find_elt(self.context_tab)

    # 找到发布文章导航栏
    def find_pub_ari_tab(self):
        return self.find_elt(self.pub_ari_tab)


# 操作层
class HomeHandle(BaseHandle):

    def __init__(self):
        self.home_page = HomePage()

    # 内容管理菜单栏点击
    def click_context_tab(self):
        self.home_page.find_context_tab().click()

    # 发布文章导航栏点击
    def click_pub_ari_tab(self):
        self.home_page.find_pub_ari_tab().click()


# 业务层
class HomeProxy:

    def __init__(self):
        self.home_handle = HomeHandle()

    # 跳转发布文章页面
    def to_pub_ari_page(self):
        # 点击内容管理菜单栏
        self.home_handle.click_context_tab()
        # 点击发布文章菜单
        self.home_handle.click_pub_ari_tab()
