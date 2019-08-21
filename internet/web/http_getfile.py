#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.parse import urlparse

res = urlparse('http://www.baidu.com/index.html')

print(res)


# import web.client
#
# sername, fname = 'www.baidu.com', '/index.html'
# conn = web.client.HTTPConnection(sername)
# conn.putrequest('GET', fname)
# conn.putheader('Accept', 'text/html')
# conn.endheaders()
#
# reply = conn.getresponse()
#
# print(reply.status)
# if 200 != reply.status:
#     print(reply.status, reply.reason)
# else:
#     list_lines = reply.readlines()
#     reply.close()
#     for line in list_lines[:6]:
#         print(line)
