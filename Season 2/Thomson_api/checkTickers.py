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

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(path)

tickers = pd.read_excel('tickerList.xlsx')
tickers = tickers[tickers['ticker'] != 'DUMMY']

# For Eikon 
#ek.set_app_key('e14c5b0ed4a6437baba5b2d6b644d9a3bd59457a')
#df_list = {}
#for i in range(len(tickers)):
#    ticker = list(np.squeeze(tickers.values))[i]
#    try:
#        df =ek.get_timeseries(ticker, fields = ["Close"] ,
#                              start_date="2019-01-01",  
#                              end_date="2019-06-30")
#        df_list[ticker] = df
#    except:
#        pass
