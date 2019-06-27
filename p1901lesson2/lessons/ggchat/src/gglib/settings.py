IO = {
    "BIND_ADDRESS": ("127.0.0.1", 6767),
    "SZ_SEND_BUFFER": 0xFFFF,
    "SZ_RECV_BUFFER": 0xFFFF, # 收发消息的最大字节
    "SOCKET_KEEPALIVE": (5, 5) #每隔5秒确定是否连接
}

NUM_WORKERS = 10

DATABASE = {
    "NAME": "mysql", # 数据库
    "OPTIONS": {
        "HOST": "",  # 主机
        "PORT": "",  # 端口
        "USER": "",  # 用户
        "PASSWORD": "",  #  密码
        "DB": ""
    }
}

LOGGER = {
    "BACKEND": "gglib.loggers.file.FileHandler", # 找到FileHandler
    "OPTIONS": {  # 日志存储的地址
        # "file": "./gg-1.log"
    },
    "LEVEL": "warn", # DEBUG, INFO, WARN, ERROR, CRITICAL # 日志的几个级别（warm前的不打印）
    "FORMAT":  "",
}

MIDDLEWARES = [
    ""
]

