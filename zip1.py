#Pyhon programe to unzip files from zip 
# import zipfile
# with zipfile.ZipFile('Core JavaScript Notes.zip', 'r') as zip_ref:
#     zip_ref.extractall('')

import zipfile
with zipfile.ZipFile("Core JavaScript Notes.zip","r") as zip_ref:
    zip_ref.extractall("D:\June-11\Java Notes JS\JS")