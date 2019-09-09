# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:25:52 2019

@author: Woojin
"""

import eikon as ek
import pandas as pd
import numpy as np
import os, inspect
import sqlite3

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(path)

conn = sqlite3.connect('DB_ver_1.0.db')  # Database 연결 (없는 경우 자동생성)
c = conn.cursor()  # you can create a Cursor object and call its 
                   # execute() method to perform SQL commands


qry = "SELECT * FROM econ"
df = pd.read_sql_query(qry, conn)


