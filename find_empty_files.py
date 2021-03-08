#!/usr/bin/env python3
import os
# import report
from shutil import copy

#src = "PPP Backup"
src = "E:\\Backup\\Actual_Backup"
copy_to = "CSVsBackupFeb21"
#copy_to = "CSVs\hdd"
# copy_to = "CSVs\computer"
created_file = "report/report3.pdf"

def search_and_copy_file(source,copy_to):
    message = ""
    count = 0
    list = []
    for subdir, dirs, files in os.walk(src):
        for filename in files:
            container = subdir + os.sep
            filepath =  container + filename
            if filepath.endswith(".csv"):
                count = count+1
                renamed_file = copy_to + "/"+str(count)+"_"+filename
                copy(filepath,renamed_file)
                statement = filename+" copied!! -->> From "+ container +"<br/><br/>"
                list.append(statement)
            
    list.append("<br/><b>Total files copied: " + str(count)+"<br/></b>")
    print(str(count) + " files copied!")
    message = message.join(list)
    return message

if __name__ == "__main__":
    message = search_and_copy_file(src, copy_to)
    title = "List of CSV files copied"
    # report.generate_report(created_file, title, message)
    print("Report created!!")
