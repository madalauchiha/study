#!/usr/loacl/bin/env python
# -*- coding: utf-8 -*-

import pymysql


conn = pymysql.connect(host='localhost',
                       port=3306,
                       user='root',
                       passwd='root',
                       db='db_test',
                       charset='utf8')

curs = conn.cursor()

# tbl_cmd = 'create table people (name char(30), job char(10), age int(4))'
# curs.execute(tbl_cmd)

# cmd_insert = 'insert into people values(%s, %s, %s)'
# curs.execute(cmd_insert, ('yunduo', 'student', 3))
# curs.executemany('insert into people values(%s, %s, %s)', ((3, '3', 3), ('4', '4', 4)))
# conn.commit()

# print(curs.rowcount)
# print(pymysql.paramstyle)

# curs.execute('select * from people where age < %s order by age', 3)
# print(curs.fetchall())

curs.execute('update people set age=%s where age < %s', (30, 34))
conn.commit()

curs.execute('delete from people where age = 30')
conn.commit()

curs.execute('select * from people')

col_names = [rec[0] for rec in curs.description]
for row in curs.fetchall():
    print(dict(zip(col_names, row)))

curs.close()
conn.close()
