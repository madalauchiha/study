#!/usr/local/python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse
import re
import subprocess
import sys
import os

try:
    subprocess.check_output(['ping', '8.8.8.8', '-c', '1', '-w', '1'])
except subprocess.CalledProcessError:
    print('internet not available!')
    sys.exit(1)

bing_url = 'https://cn.bing.com'

bing_html = urllib.request.urlopen(bing_url).read()
# open('bing.html', 'wb').write(html.read())

pat = r'href="/(th\?id=.*?jpg)'.encode()
match_obj = re.search(pat, bing_html)

relative_url = str()
if match_obj:
    relative_url = bytes.decode(match_obj.group(1))

# print(relative_url)
jpg_url = urllib.parse.urljoin(bing_url, relative_url)
print(jpg_url)

jpg = urllib.request.urlopen(jpg_url).read()
# jpg = urllib.request.urlopen(req_jpg)

dir_jpg = os.path.dirname(os.path.realpath(__file__))
path_jpg = os.path.join(dir_jpg, 'bing.jpg')
open(path_jpg, 'wb').write(jpg)

os.system('gsettings set org.gnome.desktop.background picture-uri "file:' + path_jpg + '"')
