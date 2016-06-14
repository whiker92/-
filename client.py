# -*- coding: UTF-8 -*-
__author__ = 'Whiker'
__mtime__ = '2016/6/14'
'''
socket client tcp
'''

import socket

ip = raw_input(u"输入服务端地址:")
tcp_or_udp = raw_input(u"选择TCP/UDP 1(TCP) 0(UCP)")
if tcp_or_udp == "1":
	# 创建socket IPv4&&TCP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 建立连接
	sock.connect((ip, 9999))
	print(("服务器连接成功,接收数据为:%s" % sock.recv(1024)).decode('utf-8'))
	sock.send(raw_input(u"想要发送的消息为:"))
	sock.close()

else:
	# 创建socket IPv4&&UCP
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.sendto(raw_input(u"想要发送的消息为:"), (ip, 9999))
	print(("服务器连接成功,接收数据为:%s" % sock.recv(1024)).decode('utf-8'))
	sock.close()
