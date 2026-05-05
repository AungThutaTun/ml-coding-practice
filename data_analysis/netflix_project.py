#-*- coding:utf-8 -*-
# 넷플릭스 데이터 분석 프로젝트

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 세선 저장소에 업로드한 csv 파일을 읽어 변수에 할당
netflix = pd.read_csv('netflix_titles.csv')
netflix. head()

# .columns : 열 이름 확인
list (netflix.columns)

#.head(3) : 데이터 처음 3개의 행 출력
netflix.head(3)

# .info() : 열에 대한 요약 정보 확인
netflix.info() 

# 넷플릭스 결축치 비율 확인하기
for i in netflix.columns :
    missingValueRate = netflix[i].isna().sum() / len(netflix) * 100
    if missingValueRate > 0 :
        print("{} null rate: {}%".format(i,round(missingValueRate, 2)))

# .fillna() : 결측치를 다른 값으로 대채항여 처리
#결축지 비율 : country(9.44%)
netflix['country'] =netflix['country'].fillna('No Data')  

#.replace(np.nan, 'b') : 결축치를 문자열 바꾸기 함수를 통해 처리
#결축지 비율 : director(29.91%) , cast(9.37%)
netflix['director'] = netflix['director'].replace(np.nan, 'No Data')
netflix['cast'] = netflix['cast'].replace(np.nan, 'No Data')

#.dropna(axis = 0) : 결축치가 있는 행 제거
#원본 개책를 수정하려면 inplace = True 옵션 추가
#결축지 비율 : date_add(0.11%), rating(0.05%), duration(0.03%)
netflix.dropna(axis = 0 , inplace=True)

#.info() : 열에 대한 요약 정보 확인
#8807 rows(원ㅂㅗㄴ 데이터행 개수) - 17 rows(결축지 행)) = 8790 rows(결축지가 제거된 행 개수)
netflix.info()

#데이터프레임의 각 멀럼별 결축지 개수 반환
#isna() == isnull() : 결축 값을  True로 반환하고 그외에는 False로 반환하는 함
netflix.isna().sum()
#
#시청 등급 기준표를 참고하여 Netflix의 rating 변수를 이용한 age_group_dic 변수 생성
# rating 컬럼의 값을 age_group이라는 새로운 컬럼으로 복사
netflix['age_group'] = netflix['rating']

# 시청 등급 코드를 더 이해하기 쉬은 표현으로 매핑한 딧셔너리 정의(key, value 선언)
age_group_dic = {
    'G' : 'All',
    'TV-G' : 'All',
    'TV-Y' : 'All',
    'PG' :'Older Kids',
    'TV-Y7' : 'Older Kids',
    'TV-Y7-FV' : 'Older Kids',
    'TV-PG' : 'Older Kids',
    'PG-13' : 'Teens',
    'TV-14' : 'Young Adults',
    'NC-17' : 'Adults',
    'NR' : 'Adults',
    'UR' : 'Adults',
    'R' : 'Adults'
    'TV-MA' : 'Adults'
}