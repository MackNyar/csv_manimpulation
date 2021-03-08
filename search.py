#!/usr/bin/env python3
import os
# import report
from shutil import copy

#src = "PPP Backup"
src = "C:\\Backup"
#folder = "CSVsBackupFeb21"
folder = "marchaddin"

created_file = "report/report3.pdf"

def create_path(path, name, extension, version):  
    """ Returns a joined path """
    filename = name + "_"+str(version) + extension
    return os.path.join(path, filename)

def is_file_empty(filename):
    """ Check if file is empty by reading first character in it """
    with open(filename, 'r') as file:
        first_char = file.read(1)
        if not first_char:
            return True
    return False



def search_and_copy_file(source,folder_to):
    message = ""
    count = 0
    list = []
    for subdir, dirs, files in os.walk(source):
        for filename in files:
            container = subdir + os.sep
            filepath =  container + filename
            if filepath.endswith(".csv"):
                if not is_file_empty(filepath):
                    count = count+1
                    name, extension = os.path.splitext(filename)
                    path_to =  create_path(folder_to, name, extension, count)
                    try:
                        copy(filepath,path_to)
                        print ("%s copied successfuly" % filename)
                    except Exception as e:
                        print ("Unable to copy file. %s" %e)
                else:
                    print("%s is empty. Therefore not copied" %filename)
                
                
                statement = filename+" copied!! -->> From "+ container +"<br/><br/>"
                list.append(statement)
            
    list.append("<br/><b>Total files copied: " + str(count)+"<br/></b>")
    print(str(count) + " files copied!")
    message = message.join(list)
    return message

if __name__ == "__main__":
    message = search_and_copy_file(src, folder)
    title = "List of CSV files copied"
    # report.generate_report(created_file, title, message)
    print("Report created!!")
