import pandas as pd 
#import numpy as np 

df_new = pd.read_csv('01. AllCSVsMarch2021/2021MarAllCapturedSorted.csv')

GFG = pd.ExcelWriter('01. AllCSVsMarch2021/2021MarAllCapturedSorted.xlsx')
df_new.to_excel(GFG, index = False)
GFG.save()