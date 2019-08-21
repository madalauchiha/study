#!/usr/local/bin/env python
# -*- encoding: utf-8 -*-

import os
import sys


def start(cmdline):
    if 0 == os.fork():
        os.execvp(sys.executable, ['python3'] + cmdline.split())
        os._exit(0)


for i in range(8):
    start('echo_client.py')
# start('echo_client.py')
# os.system('python echo_client.py')

# print('here')
