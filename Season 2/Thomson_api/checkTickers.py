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

tickers = pd.read_excel('tickerList_2.xlsx')
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

# For DataStream
import DatastreamDSWS as DSWS

username_ = input("USERNAME : ")
pw_ = input("PASSWORD : ") 
ds = DSWS.Datastream(username = username_, password = pw_)

df_list_2 = []
na_ticker = []
error_ticker = []
for i in range(len(tickers)):
    ticker = list(np.squeeze(tickers['ticker']))[i]
    flds = list(np.squeeze(tickers['field']))[i]
    try:
        df =ds.get_data(ticker, fields = ['X'], start="-100D", end="-0D", freq="D")
        if df.shape[1] == 3:
            na_ticker.append(ticker)
            pass
        else:
            df.columns = [ticker]
            df_list_2.append(df)
            print(ticker)
    except:
        error_ticker.append(ticker)
        pass

final_df = pd.concat(df_list_2,axis=1).stack().reset_index()
final_df.columns = ['date', 'ticker', 'value']
final_df.set_index('date', inplace=True)
final_df = final_df.sort_values('date')
final_df.to_excel('sample_DBformat.xlsx')


#final_df[final_df['ticker'] == 'USFEFRL']['value']

#
#



