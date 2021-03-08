#!/usr/bin/env python3
import os
# import report
from shutil import copy
source = "copies"
dest = "CSVs/"
for subdir, dirs, files in os.walk(source):
    for filename in files:
    	container = subdir + os.sep
    	filepath =  container + filename
    	base = os.path.splitext(filename)[0]
    	
    	try:
    		os.rename(filepath, dest +"/"+base + '.csv')
    		print("File renamed successfuly")
    	except IsADirectoryError:
    		print("Source is a file but destination is a directory")
    	except NotADirectoryError:
    		print("Source is a directory but destination is a file")

    	except PermissionError:
    		print("Operation not permmitted")
    	except OSError as error:
    		print(error)
