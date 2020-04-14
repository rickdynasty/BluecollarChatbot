import logging
import os


class Logger:
    def __init__(self, name=__name__):
        # 创建一个loggger
        self.__name = name
        self.logger = logging.getLogger(self.__name)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        # log_path = os.path.dirname(os.path.abspath(__file__))
        # logname = log_path + '/' + 'out.log'  # 指定输出的日志文件名
        # fh = logging.handlers.TimedRotatingFileHandler(logname, when='M', interval=1, backupCount=5,encoding='utf-8')  # 指定utf-8格式编码，避免输出的日志文本乱码
        # fileHandler = logging.FileHandler(logname, mode='w', encoding='utf-8')  # 不拆分日志文件，a指追加模式,w为覆盖模式
        # fileHandler.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台
        # consoleHandler = logging.StreamHandler()
        # consoleHandler.setLevel(logging.DEBUG)
        #
        # # 定义handler的输出格式
        # formatter = logging.Formatter('%(asctime)s-%(name)s-%(filename)s-[line:%(lineno)d]'
        #                               '-%(levelname)s-[日志信息]: %(message)s',
        #                               datefmt='%a, %d %b %Y %H:%M:%S')
        # # fileHandler.setFormatter(formatter)
        # consoleHandler.setFormatter(formatter)
        #
        # # 给logger添加handler
        # # self.logger.addHandler(fileHandler)
        # self.logger.addHandler(consoleHandler)

    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


log = Logger(__name__).get_log
