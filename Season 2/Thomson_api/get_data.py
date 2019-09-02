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
import arrow

path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(path)

class getData:
    
    def __init__(self, username, password):
        
        self.username_ = username
        self.password_ = password
        self.ds = DSWS.Datastream(username = self.username_, password = self.password_)

    def econData(self, tk, day_start, day_end="-0D", freq="D"):       
        df = self.ds.get_data(tickers = tk, fields = ['X'], start=day_start, end="-0D", freq=freq)
        df.columns = [tk]
        return df
    
    def NDOR(self, tk):
        '''
        Next Date of Release 의 경우 티커 하나씩 넣어야되고 여러 티커 넣음 두번째 티커부터 N/A가 나옴
        한국표준시 (도쿄 시간)로 변경 후 출력
        
        출력양식 : 날짜 (정수, 20190510), 시간 (정수, 2130)
        
        '''
        df = self.ds.get_data(tickers = tk, fields=["DS.NDOR1"])
        date_val = df[df['Datatype'] == 'DS.NDOR1_DATE']['Value'].values[0]
        time_val = df[df['Datatype'] == 'DS.NDOR1_TIME_GMT']['Value'].values[0]
        ref_date_val = df[df['Datatype'] == 'DS.NDOR1_REF_PERIOD']['Value'].values[0]
              
        seoul_dt = arrow.get(date_val + ' ' + time_val, 'YYYY-MM-DD HH:mm').to('Asia/Tokyo').datetime
        seoul_date = int(pd.to_datetime(seoul_dt).strftime("%Y%m%d"))
        seoul_time = int(pd.to_datetime(seoul_dt).strftime("%H%M"))  
        
        ref_date_val = int(str(ref_date_val[:4])+str(ref_date_val[5:7])+ref_date_val[8:10])
        
        return seoul_date, seoul_time, ref_date_val
    
    def GEOGN(self, tk):
        '''
        GEOGN - Geographical Classification Of Company (Name)
        '''           
        df = self.ds.get_data(tickers = tk, fields=["GEOGN"], kind = 0)
        geo = df['Value'].values        
        return geo
    
    
