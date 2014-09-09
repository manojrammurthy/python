import os

def rename_files():
    #1 to get names of files in a folder
    filelist= os.listdir(r"/home/lenovo/Downloads/prank/prank")
    print(filelist)
    saved_path = os.getcwd()
    print "current working directory is "+saved_path
    os.chdir(r"/home/lenovo/Downloads/prank/prank")
    #2 for each file rename file 
    for file_name in filelist:
        os.rename(file_name,file_name.translate(None, "0123456789"))
    os.chdir(saved_path)
rename_files()