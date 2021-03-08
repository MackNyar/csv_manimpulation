# importing pandas package 
import os
import csv

path = "C:\\productimages"
heading = "barcode"
rows = []
barcodes = os.listdir(path)
for barcode in barcodes:
	rows.append([barcode])

with open("barcodes_030321.csv", 'w',newline="") as f:
	writer = csv.writer(f)
	writer.writerows(rows)



