# 日志
from gglib.settings import LOGGER

__all__ = ["LOG_LEVEL", "debug", "info", "warn", "error"] # 引入的几个模块

LOG_LEVEL = { #  日志的几个等级
    "debug": 1,
    "info": 2,
    "warn": 3,
    "error": 4
}


class BaseLogger:   # 引用file里面的方法
    def __init__(self, level, fmt="", **kwargs):
        self.level = level
        self.fmt = fmt

    def info(self, sender, *args):
        raise NotImplementedError

    def debug(self, sender, *args):
        raise NotImplementedError

    def warn(self, sender, *args):
        raise NotImplementedError

    def error(self, sender, *args):
        raise NotImplementedError


import importlib
import pdb

# pdb.set_trace()

# 获取LOGGER配置信息
_backend = LOGGER['BACKEND']
# 将'BACKEND'字段分割成 module, class
_module, _cls = _backend.rsplit(".", 1)
# 导入指定module
_logger_module = importlib.import_module(_module)
# 从导入的module里面获取class
_logger_cls = getattr(_logger_module, _cls)
# 验证类
if not issubclass(_logger_cls, BaseLogger):
    raise ImportError("The {} class must be subclass of the BaseLogger".format(_logger_cls.__name__))
# 实例化class
_logger_handler = _logger_cls(LOGGER['LEVEL'], LOGGER['FORMAT'], **LOGGER['OPTIONS'])

# 获取实例的方法
debug = _logger_handler.debug
info = _logger_handler.info
warn = _logger_handler.warn
error = _logger_handler.error