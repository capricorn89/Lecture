# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:25:52 2019

@author: Woojin
"""

##  Eikon 사용 가능 티커 정리

import eikon as ek
import pandas as pd
import numpy as np
import os, inspect
import DatastreamDSWS as DSWS

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(path)

tickers = pd.read_excel('tickerList_2.xlsx')
tickers = tickers[tickers['ticker'] != 'DUMMY']

username_ = input("USERNAME : ")
pw_ = input("PASSWORD : ") 
ds = DSWS.Datastream(username = username_, password = pw_)

tick = '@NTSX'

df  = ds.get_data(tickers = tick, fields = ['NAME'], kind = 0)