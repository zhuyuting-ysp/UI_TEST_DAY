# 对象库层-基类，把定位元素的方法定义在基类中
from utils import DriverUtils


# 1.定义对象库层的基类
class BasePage:

    def __init__(self):
        # 获取浏览器驱动对象
        self.driver = DriverUtils.get_mis_driver()

    # 2.公用的元素定位方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 1.定义操作层的基类
class BaseHandle:

    # 2.定义公用的元素输入方法
    def input_text(self, element, text):
        # 清空用户名输入框默认值
        element.clear()
        # 通过表示对象库层的实例属性来获取用户名输入框的元素对象,并执行输入
        element.send_keys(text)
