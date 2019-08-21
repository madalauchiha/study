#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import signal
import sys


def on_signal(sig_num, stack_frame):
    print('got signal %d' % sig_num)


sig_num = int(sys.argv[1])
signal.signal(sig_num, on_signal)
while True:
    signal.pause()
