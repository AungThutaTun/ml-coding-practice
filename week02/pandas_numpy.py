import pandas as pd

file_url ='https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample.csv'
sample = pd.read_csv(file_url)

print(sample.head())
print(sample.tail())

sample.info()
sample.describe()

sample_dic ={'name': ['John', 'Ann', 'Kevin'], 'age': [23,22,21]}
a = pd.DataFrame(sample_dic)

a.info()

pd.DataFrame([[1,2,],[3,4],[5,6],[7,8]])
pd.DataFrame([[1,2,],[3,4],[5,6],[7,8]], columns=['var_1', 'var_2'], index= ['a','b','c','d'])

import pandas as pd
file_url='https://media.githubusercontent.com/media/musthave-ML10/data_source/main/sample_df.csv'

sample_df = pd.read_csv(file_url, index_col=0)
print(sample_df.head())

print(sample_df['var_5'])

#print(sample_df['var_1', 'var_2]) #[] 안에난 하나의ㅜ값만 들어갈 수 있음
print(sample_df[['var_1', 'var_4']]) # [ []]를 사용하면 [] 가 하나의 값이 인식됨

#loc 는 location의 앞글자
print(sample_df.loc['a'])       #행 기둔으로 인덱싱
print(sample_df.loc[['a', 'c', 'e']])
print(sample_df.loc['a':'c'])

#iloc 는 index location의 앞자
print(sample_df.iloc[[0,1,2]])
print(sample_df.iloc[0,2])    
print(sample_df.iloc[0:3])
print(sample_df.iloc[0:3, 2:4])     #컬럼까지 동시에 인덱싱

print(sample_df.drop(['var_1', 'var_3'], axis=1))   #컬럼을 삭제거하려면 axis=1을 지정해야함
print(sample_df.drop(['var_1', 'var_2'],))


