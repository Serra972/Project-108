import random
import csv
import pandas as pd 
import plotly.figure_factory as px
# result=[]
# count =[]
# for i in range(0,100):
#     d1=random.randint(1,6)
#     d2=random.randint(1,6)
#     result.append (d1+d2)
#     count.append(i)
# print(result)  
# graph=px.create_distplot([result],['result'])
# graph.show()
cf=pd.read_csv('data1.csv')
ht =cf['Avg Rating'].tolist()
graph=px.create_distplot([ht],['Avg Rating'],show_hist = False)
graph.show()