# 定义测试类
import time
import logging

import allure

import config
import pytest

from page.mp.home_page import HomeProxy
from page.mp.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, get_case_data, get_allure_png


# 定义测试类
@pytest.mark.run(order=3)
class TestPubAritcle:

    def setup_class(self):
        # 1.打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建首页业务层的对象
        self.home_proxy = HomeProxy()
        # 创建发布文章业务层的对象
        self.pub_ari_proxy = PubAriProxy()
        # 创建登录页面的业务层对象

    def setup_method(self):
        self.driver.get("http://ttmp.research.itcast.cn/")

    # 定义测试方法
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.parametrize(("ari_title", "ari_context", "ari_channel", "expect"),
                             get_case_data("./data/mp/test_pub_ari_data.json"))
    def test_pub_ari(self, ari_title, ari_context, ari_channel, expect):
        # 2.组织测试数据
        # config.PUB_ARI_TITLE = ari_title.format(time.strftime("%H%M%S"))
        config.PUB_ARITCAL_TITLE = ari_title.format(time.strftime("%H%M%S"))
        print("发布文章标题{}".format(config.PUB_ARITCAL_TITLE))
        # 3.执行测试步骤
        self.home_proxy.to_pub_ari_page()
        self.pub_ari_proxy.test_pub_aritcal(config.PUB_ARITCAL_TITLE, ari_context, ari_channel)
        # 截图
        get_allure_png(self.driver,"发布文章")
        # 4.结果断言
        assert is_element_exist(self.driver, expect)

    # 5.关闭浏览器
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
