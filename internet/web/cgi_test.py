#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse

params = urllib.parse.urlencode({'usr': 'aaa', 'passwd': 'bbb'})
# print(params)
rsp = urllib.request.urlopen('http://localhost/cgi-bin/test.py?' + params)
print(rsp.read().decode())
