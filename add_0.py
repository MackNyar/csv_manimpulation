# importing pandas package 
import pandas as pd 
  
# making data frame from csv file 
col_list = ["barcode","length","width","height"]
data = pd.read_csv("final/all_cleaned.csv", usecols=col_list)
# def str_replace(text):
# 	to_str = str(text)
# 	return to_str.replace('.0','').strip()

measurements_list = []

for index, row in data.iterrows():
	barcode = row["barcode"]
	length = row["length"]
	width = row["width"]
	height = row["height"]
	if (len(barcode) == 12) or (len(barcode) == 7):
		long_barcode = "0"+ barcode
		measurements_list.append([long_barcode, length, width, height])
	else:
		measurements_list.append([barcode, length, width, height])

df = pd.DataFrame(measurements_list)
df.columns= ["barcode", "length", "width", "height"]
df.to_csv("final/all_cleaned_01.csv", sep=",", encoding="utf-8",index=False)







	
#data["barcode"].to_csv("barcodes.csv", sep=",", encoding="utf-8",index=False)