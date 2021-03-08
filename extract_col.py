# importing pandas package 
import pandas as pd 
  #C:\Users\My China\Desktop\Grouped CSVs\AllCSVsFeb2020
# making data frame from csv file 
col_list = ["barcode","length","width","height"]
data = pd.read_csv("01. AllCSVsMarch2021/2021MarAllCapturedSorted.csv", usecols=col_list) 
data["barcode"].to_csv("01. AllCSVsMarch2021/AllSortedBarcodes.csv", sep=",", encoding="utf-8",index=False)
print(data["barcode"])

