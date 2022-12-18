from zipfile import ZipFile

# file = 'D:\Ress_Proj\startbootstrap-modern-business-gh-pages.zip'

with ZipFile("D:\Ress_Proj\startbootstrap-modern-business-gh-pages.zip",'r') as zobj:
    zobj.extractall(
        path = 'D:\Ress_Proj\extract')