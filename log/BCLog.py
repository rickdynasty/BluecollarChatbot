import logging
import logging.config
import os
import sys


class Logger:
    def __init__(self, name=__name__):
        # 创建一个loggger
        self.__name = name

        logconfigname = 'logconfig.ini'
        if 'actions' in sys.argv:
            logconfigname = 'logconfig-rasa-actions.ini'
        else:
            logconfigname = 'logconfig-rasa.ini'

        log_config_path = os.path.dirname(os.path.abspath(__file__))+'/'+logconfigname
        logging.config.fileConfig(log_config_path)
        self.logger = logging.getLogger(name)



    @property
    def get_log(self):
        """定义一个函数，回调logger实例"""
        return self.logger


log = Logger(__name__).get_log
