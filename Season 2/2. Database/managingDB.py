# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:44:42 2019

@author: check
"""

import os, inspect
import sqlite3
import pandas as pd

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(path)

samplefile = pd.read_excel('sample_DBformat.xlsx')
samplefile.drop_duplicated(inplace=True)
samplefile.reset_index(drop=True, inplace=True)

conn = sqlite3.connect('DB_example.db')  # Database 연결 (없는 경우 생성까지)

c = conn.cursor()  # you can create a Cursor object and call its 
                   # execute() method to perform SQL commands

# 데이터를 넣기 위한 테이블 생성
c.execute('''CREATE TABLE econ (date text, ticker text, value real)''')

'''
<예시>

table명 : econ
_____________________________________
date        |  ticker     |  value
_____________________________________
2019-01-01  |  USFEFRL    |  2.00
-------------------------------------
2019-01-01  |  USFEFRH    |  2.25
-------------------------------------
2019-02-01  |  USFEFRL    |  2.25
-------------------------------------
'''

# Pandas 데이터프레임 형태로 불러온 데이터를 econ 테이블에 삽입
samplefile.to_sql('econ', conn, if_exists = 'replace')

# 잘 들어갔는지 확인
pd.read_sql_query("select * from econ;", conn)


# 기존 데이터의 업데이트 (내용 변경의 가능성이 있으니)

def update_value(ticker_, date_, val):
    conn = sqlite3.connect('DB_example.db')  # Database 연결 (없는 경우 생성까지)
    c = conn.cursor()  
    query = "UPDATE econ SET value="
    query += str(val)
    query += " where date='"
    query += str(date_)
    query += "' and ticker='"
    query += str(ticker_)
    query += "'"
    c.execute(query)
    conn.commit()

pd.read_sql_query("select * from econ where date='2019-08-30' and ticker='IDPRATE.'", conn)



