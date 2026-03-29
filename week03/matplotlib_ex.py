#-*- coding: utf-8 -*-
# 타이타닉 데이터셋 불러오기
import pandas as pd

#티이타닉 CSV 파일 불러오기
titanic = pd. read_csv('3.1.1.titanic.csv')

# head() 함수를 출력하여 타이타닉 데이터셋의 구성을 간단히 살펴보기


print(titanic.head())


print(titanic.info())

""" ###"""


pclass_survived_mean = titanic.groupby('Pclass') ['Survived'].mean().reset_index()
pclass_survived_mean


import matplotlib.pyplot as plt


plt.plot(pclass_survived_mean['Pclass'], pclass_survived_mean['Survived'],
         marker='o', linestyle='-', color='violet')
plt.title('Survival Rate Variation Across Passenger Classes')
plt.xlabel('Pclass')
plt.ylabel('Survival Rate')
plt.xticks([1, 2, 3])
plt.grid(True)
plt.savefig('Figure01.png')
plt.close()




survived_counts = titanic[titanic['survived'] == 1] ['Embarked']. value_counts()
print(survived_counts)