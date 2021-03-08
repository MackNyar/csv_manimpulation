# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
col_list = ["barcode","length","width","height"]
data = pd.read_csv("01. AllCSVsMarch2021/2021MarAllCapturedSorted.csv", usecols=col_list)
def str_replace(text):
	to_str = str(text)
	return to_str.replace('.0','').strip()

measurements_list = []

for index, row in data.iterrows():
	barcode = str_replace(row["barcode"])
	length = str_replace(row["length"])
	width = str_replace(row["width"])
	height = str_replace(row["height"])
	measurements_list.append([barcode, length, width, height])

df = pd.DataFrame(measurements_list)
df.columns= ["barcode", "length", "width", "height"]
df.to_csv("01. AllCSVsMarch2021/2021MarAllCapturedSorted_2.csv", sep=",", encoding="utf-8",index=False)







	
#data["barcode"].to_csv("barcodes.csv", sep=",", encoding="utf-8",index=False)