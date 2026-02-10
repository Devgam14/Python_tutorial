abs_path = "C:\\Users\AURAGAM\Desktop\\PythonTutorial\\FileHandling\\user_data.txt"
## always remember to add r to your path url as the escape sequence handler or add the second slash \\
rel_path = r"FileHandling\user_data2.txt"
fh = open(rel_path)
data = fh.read()
print(data)
## when using the formal method always remember to close the file 
fh.close()   
## the fh has a property to check whether is closed                   
if fh.closed :
    print("file is closed")