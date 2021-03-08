import os, glob
import pandas as pd

dir = "20210224"
for file in os.listdir(dir):
    df = pd.read_csv(dir +"/" + file, header=None)
    df.to_csv("20210224"+file, header=["barcode", "length", "width", "height"], index=False)
