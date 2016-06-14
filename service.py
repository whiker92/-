# -*- coding: UTF-8 -*-
import threading
import socket
import select

__author__ = 'Whiker'
__mtime__ = '2016/6/14'
'''
socket service tcp
'''


def tcplink(sock, addr):
	print(u"服务端接收来自%s的tcp消息." % addr[0])
	sock.send("你好!我是服务端.")
	data = sock.recv(1024)
	print(u"收到%s的信息:%s" % (addr[0], data))
	sock.close()
	print(u"与%s的连接断开." % addr[0])


socktcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socktcp.bind(('0.0.0.0', 9999))
socktcp.listen(5)

sockudp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockudp.bind(('0.0.0.0', 9999))

while True:
	infdstcp, outfds, errfds = select.select([socktcp, ], [], [], 3)
	infdsudp, outfds, errfds = select.select([sockudp, ], [], [], 2)
	if len(infdstcp) != 0:
		s, addr = socktcp.accept()
		t = threading.Thread(target=tcplink, args=(s, addr))
		t.start()
	if len(infdsudp) != 0:
		data, addr = sockudp.recvfrom(1024)
		print(u"服务端接收来自%s的udp消息%s." % (addr[0], data))
		sockudp.sendto("你好!我是服务端.", addr)
	print(u"服务器等待连接...")
