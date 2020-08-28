# 1.导包
import unittest

from parameterized import parameterized

from page.app.index_page import IndexProxy
from utils import DriverUtils, is_el_by_attribute


# 2.定义测试类
class TestQyAritcal(unittest.TestCase):

    # 3.定义初始化方法
    @classmethod
    def setUpClass(cls):
        # 获取app驱动对象
        cls.driver = DriverUtils.get_app_driver()
        # 创建首页业务层对象
        cls.index_proxy = IndexProxy()

    def setUp(self):
        self.driver.start_activity("com.itcast.toutiaoApp", ".MainActivity")

    # 4.定义测试方法
    @parameterized.expand(["架构", "linux"])
    def test_qy_aritcal(self,channel_name):
        # 组织测试数据
        # channel_name = "架构"
        # 调用根据频道查询文章的业务方法
        self.index_proxy.test_qari_by_channel(channel_name)
        # 断言
        self.assertTrue(is_el_by_attribute(self.driver, "text", "点赞"))

    # 5.定义销毁方法
    @classmethod
    def tearDownClass(cls):
        DriverUtils.quit_app_driver()
