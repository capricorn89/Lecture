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

import get_data as get

user = input("USERNAME : ")
pw = input("PASSWORD : ") 

DS = get.getData(user, pw)

DS.econData('USUNCLM', '-50D', freq = 'M')

dt, time, __ = DS.NDOR('CNCONPRCF')

DS.GEOGN('USCNFCONX, CNCONPRCF')