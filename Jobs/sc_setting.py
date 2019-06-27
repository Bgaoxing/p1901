# # -*- coding: utf-8 -*-
#
# # Scrapy settings for demo1 project
# #
# # For simplicity, this file contains only settings considered important or
# # commonly used. You can find more settings consulting the documentation:
# #
# #     http://doc.scrapy.org/en/latest/topics/settings.html
# #     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# #     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#
# BOT_NAME = 'demo1'  # Scrapy项目的名字,这将用来构造默认 User-Agent,当您使用 startproject 命令创建项目时其也被自动赋值。
#
# SPIDER_MODULES = ['demo1.spiders']  # Scrapy搜索spider的模块列表 默认: [xxx.spiders]
# NEWSPIDER_MODULE = 'demo1.spiders'  # 使用 genspider 命令创建新spider的模块。默认: 'xxx.spiders'
#
# # 爬取的默认User-Agent，除非被覆盖
# 大多数情况下，网站都会根据我们的请求头信息来区分你是不是一个爬虫程序，如果一旦识别出这是一个爬虫程序，很容易就会拒绝我们的请求，
# 因此我们需要给我们的爬虫手动添加请求头信息，来模拟浏览器的行为，但是当我们需要大量的爬取某一个网站的时候，一直使用同一个User-Agent
# 很容易被识别。
# # USER_AGENT = 'demo1 (+http://www.yourdomain.com)'
#
# # 如果启用,Scrapy将会采用 robots.txt策略
# 通俗来说， robots.txt 是遵循 Robot协议 的一个文件，它保存在网站的服务器中，它的作用是，告诉搜索引擎爬虫，本网站哪些目录下的网页 不希望
# 你进行爬取收录。在Scrapy启动后，会在第一时间访问网站的 robots.txt 文件，然后决定该网站的爬取范围。
# 当然，我们并不是在做搜索引擎，而且在某些情况下我们想要获取的内容恰恰是被 robots.txt 所禁止访问的。所以，某些时候，我们就要将此配置项设置为 False ，拒绝遵守 Robot协议 ！

# ROBOTSTXT_OBEY = True
#
# # Scrapy downloader 并发请求(concurrent requests)的最大值,默认: 16
# # CONCURRENT_REQUESTS = 32
#
# # 为同一网站的请求配置延迟（默认值：0）
# # See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# # See also autothrottle settings and docs
# # DOWNLOAD_DELAY = 3   下载器在下载同一个网站下一个页面前需要等待的时间,该选项可以用来限制爬取速度,减轻服务器压力。同时也支持小数:0.25 以秒为单位
#
# # CONCURRENT_REQUESTS_PER_DOMAIN = 16   对单个网站进行并发请求的最大值。
# # CONCURRENT_REQUESTS_PER_IP = 16       对单个IP进行并发请求的最大值。如果非0,则忽略 CONCURRENT_REQUESTS_PER_DOMAIN 设定,使用该设定。 也就是说,并发限制将针对IP,而不是网站。该设定也影响 DOWNLOAD_DELAY: 如果 CONCURRENT_REQUESTS_PER_IP 非0,下载延迟应用在IP而不是网站上。
#
# # 禁用Cookie（默认情况下启用）
# # COOKIES_ENABLED = False
#
# # 禁用Telnet控制台（默认启用）
# Telnet：Scrapy有一个内建的telnet控制台，这个控制台提供了一个Python shell，
# 可以在上面运行Scrapy程序。TELNETCONSOLE_ENABLED默认情况下是启用的。TELNETCONSOLE_PORT
# 选项设置了联系控制台的端口，有时需要重新设置以防冲突。


# # TELNETCONSOLE_ENABLED = False
#
# # Scrapy HTTP Request使用的默认header：
# # DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# # }
#
# # 启用或禁用蜘蛛中间件
# # See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
# # SPIDER_MIDDLEWARES = {
# #    'demo1.middlewares.Demo1SpiderMiddleware': 543,
# # }
#
# # 启用或禁用下载器中间件
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
# # DOWNLOADER_MIDDLEWARES = {
# #    'demo1.middlewares.MyCustomDownloaderMiddleware': 543,
# # }
#
# # 启用或禁用扩展程序
# # See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
# # EXTENSIONS = {
# #    'scrapy.extensions.telnet.TelnetConsole': None,
# # }
#
# # 配置项目管道
# # See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# # ITEM_PIPELINES = {
# #    'demo1.pipelines.Demo1Pipeline': 300,
# # }
#
# # 启用和配置AutoThrottle扩展 该扩展能根据 Scrapy 服务器及您爬取的网站的负载自动限制爬取速度
# # See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# # AUTOTHROTTLE_ENABLED = True
#
# # 初始下载延迟
# # AUTOTHROTTLE_START_DELAY = 5
#
# # 在高延迟的情况下设置的最大下载延迟
# # AUTOTHROTTLE_MAX_DELAY = 60
#
#
# # Scrapy请求的平均数量应该并行发送每个远程服务器
# # AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#
# # 启用显示所收到的每个响应的调节统计信息：
# # AUTOTHROTTLE_DEBUG = False
#
# # 启用和配置HTTP缓存（默认情况下禁用）
# # See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# # HTTPCACHE_ENABLED = True
# # HTTPCACHE_EXPIRATION_SECS = 0
# # HTTPCACHE_DIR = 'httpcache'
# # HTTPCACHE_IGNORE_HTTP_CODES = []
# # HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
#
# 解释几个参数：
#
# ROBOTSTXT_OBEY = True - ----------是否遵守robots.txt
#
# CONCURRENT_REQUESTS = 16 - ----------开启线程数量，默认16
#
# AUTOTHROTTLE_START_DELAY = 3 - ----------开始下载时限速并延迟时间
#
# AUTOTHROTTLE_MAX_DELAY = 60 - ----------高并发请求时最大延迟时间
#
# 最底下的几个：是否启用在本地缓存，如果开启会优先读取本地缓存，从而加快爬取速度，视情况而定
#
# HTTPCACHE_ENABLED = True
#
# HTTPCACHE_EXPIRATION_SECS = 0
#
# HTTPCACHE_DIR = 'httpcache'
#
# HTTPCACHE_IGNORE_HTTP_CODES = []
#
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
#
# 以上几个可以视项目需要开启，但是有两个参数最好每次都开启，而每次都是项目文件手动开启不免有些麻烦，最好是项目创建后就自动开启
#
# # DEFAULT_REQUEST_HEADERS = {
# #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# #   'Accept-Language': 'en',
# # }
#
# 这个是浏览器请求头，很多网站都会检查客户端的headers，比如豆瓣就是每一个请求都检查headers的user_agent，否则只会返回403，可以开启
