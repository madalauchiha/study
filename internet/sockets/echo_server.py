#!/usr/loacl/bin/python env
# -*- coding: utf-8 -*-

import socket
import time

sockobj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockobj.bind(('', 50007))
sockobj.listen(5)

while True:
    conn, addr = sockobj.accept()
    print('Server connected by ' + str(addr))

    while True:
        data = conn.recv(1024)

        time.sleep(1)

        if not data:
            break
        print('Server recv data=> ' + str(data))
        conn.send(b'echo=> ' + data)

    conn.close()
