翻墙教程

购买服务器
https://bwh88.net/aff.php?aff=23850
得到ip端口号和密码  用户默认都是root

进入服务器
ssh root@100.160.45.201 -p 123456
这个是购买服务器分配的端口和地址然后输入密码
安装pip
安装指南地址 https://pip.pypa.io/en/stable/installing/
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
安装shadowsocks
pip install shadowsocks
yum install vim
安装vim
然后配置服务器
vim shadowsocks.conf 一下内容
{
 "server":"my_server_ip", #填入你购买的服务器IP地址
 "local_address": "127.0.0.1",
 "local_port":1080, 
"port_password": {
    "8381": "foobar1",  #端口号，密码，你要分配给自己使用的端口号和密码
    "8382": "foobar2",#端口号40000到60000之间
   "8383": "foobar3",
   "8384": "foobar4"
 },
 "timeout":300,
 "method":"aes-256-cfb",
 "fast_open": false
}
保存退出

ssserver -c shadowsocks.conf -d start

服务器配置完成

windows电脑
https://github.com/shadowsocks/shadowsocks-windows
安装软件配置IP地址端口和密码即可

Mac电脑
第一种情况  shadowsock软件可用的情况下和windows一样
第二种情况 通过命令行进行
本地安装pip和shadowsock
本机安装pip
官网教程地址https://pip.pypa.io/en/stable/installing/
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
sudo python get-pip.py或python get-pip.py
安装shadowsocks
pip install shadowsocks 或sudo pip install shadowsocks
vim shadowsocks.conf 以下内容

{
  "server":"172.96.239.85", # 服务器ip
  "server_port":38102,         #服务器上分配使用的端口，不是服务器的总端口号
  "local_address": "127.0.0.1",
  "local_port":11081,
"password":"shabigcd",  #密码
  "timeout":300,
  "method":"aes-256-cfb",
  "fast_open": true,
  "workers": 1
}

 然后运行
sslocal -c shadowsocks.conf -d start
然后安装谷歌浏览器 下载switchyomega软件
安装谷歌浏览器打开更多工具里的扩展程序
把switchyomega软件拉到浏览器的扩展程序里安装
然后设置
新建情景模式
代理协议socks5
代理服务器127.0.0.1
端口11081
然后启用这个情景模式就ok了
