#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import http.server
import os

# web_dir = '/home/dingding'
web_dir = '.'
port = 80

os.chdir(web_dir)
ser_addr = ('localhost', port)
ser_obj = http.server.HTTPServer(ser_addr, http.server.CGIHTTPRequestHandler)
ser_obj.serve_forever()
