# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
data = pd.read_csv("final/all_refined.csv") 
  
# sorting by first name 
data.sort_values("barcode", inplace = True) 
data.to_csv("all_sorted.csv", sep=",", encoding="utf-8",index=False)