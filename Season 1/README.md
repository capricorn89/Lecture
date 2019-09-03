# Lecture

#### References:
* http://pandas.pydata.org/pandas-docs/version/0.24/pandas.pdf

## I. To-do
* 1999년 3분기부터 2019년 1분기까지 데이터를 가지고, 2000년부터 매분기 둘째 달 말을 기준으로, 최근 PER가 최근 5년 평균보다 낮은 종목 30개를 골라서 투자할 경우의 누적 성과 계산 --> Time Series Data

## II. Basics (1~2주차 예상)
* Anaconda, Spyder, Jupyter
* Loop, Condition, Function
* Packages (Numpy, Pandas)

## III. Project (3~5주차 예상)

#### 0. Intro
- Pandas?
- import pandas as pd

#### 1. Import Data (API, Excel 등을 이용한 데이터 로드)
- read_excel

#### 2. Data Manipulation I 
- Indexing & Slicing (loc, iloc, isin, where..) -->  날짜, 종목 이름 등으로 데이터 뽑아내기
- Datetime & Resample  --> 시계열 데이터를 다루기 위한 툴
- Merge & Concatenation --> 두 개의 테이블 병합

#### 3. Data Manipulation II 
- nlargest, nsmallest, rank --> 특정 열 기준으로 줄세우기, 큰거 N개, 작은거 N개 고르기
- Rolling-mean --> 이동평균 등을 계산
- Aggregation (apply..)  --> 테이블 단위로 한꺼번에 함수 적용

#### 4. Plotting (생략 가능)



## IV. Further Thoughts
