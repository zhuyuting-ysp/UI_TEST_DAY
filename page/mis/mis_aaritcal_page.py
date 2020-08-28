"""
后台管理系统——审核文章
"""
#  对象库层
import time

from selenium.webdriver.common.by import By
from base.mis_base.base_page import BasePage, BaseHandle
from utils import check_channel_option, DriverUtils


class MisAtcalPage(BasePage):

    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title_box = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 选择频道 ——>之前有封装过一个公用下拉框选择的方法
        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, ".find")
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过确认按钮
        # self.pass_confirm_btn = (By.CSS_SELECTOR,".el-button--primary']")
        # 通过/驳回确认按钮
        # self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary']")
        self.con_rej_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # 找到文章标题搜索输入框
    def find_ari_title_box(self):
        return self.find_elt(self.ari_title_box)

    # 找到查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # 找到通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # 找到驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # 找到通过确认按钮
    def find_con_rej_btn(self):
        return self.find_elt(self.con_rej_btn)


# 操作层
class MisAtcalHandle(BaseHandle):

    def __init__(self):
        self.mis_atcal_page = MisAtcalPage()

    # 文章标题搜索输入框输入
    def input_ari_title(self, ari_title):
        # 找到文章标题的输入框元素对象
        element = self.mis_atcal_page.find_ari_title_box()
        # 调用父类的模拟输入的方法
        self.input_text(element, ari_title)

    # 选择文章状态
    def check_ari_status(self, ari_status):
        # 调用utils中公用的下拉框选择方法
        check_channel_option(DriverUtils.get_mis_driver(), "请选择状态", ari_status)

    # 查询按钮点击
    def click_query_btn(self):
        self.mis_atcal_page.find_query_btn().click()

    # 审核通过按钮点击
    def click_aduit_pass_btn(self):
        self.mis_atcal_page.find_pass_btn().click()

    # 驳回按钮点击
    def click_regic_btn(self):
        self.mis_atcal_page.find_reject_btn().click()

    # 审核通过/驳回按钮点击
    def click_confim_btn(self):
        self.mis_atcal_page.find_con_rej_btn().click()


# 业务层
class MisAtcalProxy:
    def __init__(self):
        self.mis_at_hl = MisAtcalHandle()

    # 审核通过测试用例
    def test_aduit_pass(self, ari_title):
        # 2.输入搜素的文章名称
        self.mis_at_hl.input_ari_title(ari_title)
        # 3.选择文章状态
        self.mis_at_hl.check_ari_status("待审核")
        # 4.点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)
        # 5.点击通过按钮
        self.mis_at_hl.click_aduit_pass_btn()

        # 6.点击提示框的确认按钮
        self.mis_at_hl.click_confim_btn()

        # 7.选择文章状态为：审核通过
        self.mis_at_hl.check_ari_status("审核通过")

        # 8.点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)


    # 驳回测试用例
    def test_reject(self):
        # # 2.输入搜素的文章名称
        # self.mis_at_hl.input_ari_title(ari_title)

        # 3.选择文章状态
        self.mis_at_hl.check_ari_status("待审核")

        # 4.点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)

        # 5.点击通过按钮
        self.mis_at_hl.click_regic_btn()

        # 6.点击提示框的确认按钮
        self.mis_at_hl.click_confim_btn()
        time.sleep(3)

        # 7.切换审核失败界面
        self.mis_at_hl.check_ari_status("审核失败")

        # 8.点击查询按钮
        self.mis_at_hl.click_query_btn()
        time.sleep(3)