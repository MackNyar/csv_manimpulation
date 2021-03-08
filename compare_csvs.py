import os
import glob
import pandas as pd

file_one = "extract_barcodes/barcodes.csv"
file_two = "extract_barcodes/col.csv"

df1 = pd.read_csv(file_one)
df2 = pd.read_csv(file_two)

# csv_df = df2[df2['barcode'].isin(df1['barcode'])]
# csv_df.to_csv("extract_barcodes/temp.csv")
# print(csv_df)

main_df = pd.concat([df1], [df2])
main_df = main_df.reser_index(drop=True)


df_grpby = main_df.groupby(list(df.columns))

idx = [x[0] for x in df_grpby.groups.values() if len(x) == 1]

print(df.reindex(idx))