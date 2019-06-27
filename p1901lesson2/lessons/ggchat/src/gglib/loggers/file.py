# 总的来说，os模块负责程序与操作系统的交互，提供了访问操作系统底层的接口；
# sys模块负责程序与python解释器的交互，提供了一系列的函数和变量，用于操控python的运行
# 时环境。一个python程序可以不用到os，但无法避免sys的介入（尽管你可能并不import它）
import datetime
import sys
from gglib.logger import BaseLogger, LOG_LEVEL

class FileHandler(BaseLogger):
    def __init__(self, level, fmt, file=None):
        super().__init__(level, fmt)
        if not file:
            self._file = sys.stdout # 标准输出到控制台
        else:
            self._file = open(file, "w")

    def __output_log(self, level, sender, message): # 日志等级，发送方，消息
        if LOG_LEVEL[level] >= LOG_LEVEL[self.level]: # 判断打印的日志信息（等级）
            self._file.write("{} {} {}: {}\n".format(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"),
                                                     sender,
                                                     level,
                                                     message))

    def debug(self, sender, *args):
        self.__output_log("debug", sender, *args)

    def info(self, sender, *args):
        self.__output_log("info", sender, *args)

    def warn(self, sender, *args):
        self.__output_log("warn", sender, *args)

    def error(self, sender, *args):
        self.__output_log("error", sender, *args)