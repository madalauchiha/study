#!/usr/local/bin/env python
# -*- coding: utf-8 -*-

import dbm

dbm_file = dbm.open('dbm', 'c')
dbm_file['name'] = 'dingding'

print(dbm_file.keys())
print(dbm_file['name'])

dbm_file.close()
