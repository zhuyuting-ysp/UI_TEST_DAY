import logging.handlers
# 发布文章标题数据
PUB_ARITCAL_TITLE = None

# 日志打印基础配置方法
def log_basic_config():
    # 1.创建日志器
    logger = logging.getLogger()
    # 2.设置日志级别
    logger.setLevel(logging.INFO)
    # 3.创建处理器
    ls = logging.StreamHandler()
    lnt = logging.handlers.TimedRotatingFileHandler("./log/hmtt_test.log", when="midnight", interval=1, backupCount=2)
    # 4.创建格式化器
    formatter = logging.Formatter(
        fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s')
    # 5.将格式化器绑定到处理器
    ls.setFormatter(formatter)
    lnt.setFormatter(formatter)
    # 6.将处理器添加到日志
    logger.addHandler(ls)
    logger.addHandler(lnt)

