# abs_path = "C:\\Users\AURAGAM\Desktop\\PythonTutorial\\FileHandling\\user_data.txt"
## always remember to add r to your path url as the escape sequence handler or add the second slash \\
rel_path = r"FileHandling\user_data2.txt"
with open(rel_path) as fs:
    data = fs.readlines()[2]
    print(data)