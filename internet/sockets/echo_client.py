#!/usr/loacl/bin/python env
# -*- coding: utf-8 -*-

import socket

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.connect(('localhost', 50007))

sockobj.send(b'Hello, world!')
data = sockobj.recv(1024)
print('Client recv data=>', str(data))

sockobj.close()
