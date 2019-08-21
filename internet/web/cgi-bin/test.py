#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

form = cgi.FieldStorage()

print('Content-type: text/html\n')
print('<hr>')

if 'usr' not in form:
    print('name get error</br>')
else:
    print('name: %s</br>' % form['usr'].value)
if 'passwd' not in form:
    print('password get error')
else:
    print('password: %s' % form['passwd'].value)

print('<hr>')