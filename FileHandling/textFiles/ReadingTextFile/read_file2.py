abs_path = r"C:\\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_data.txt"
rel_path = r"FileHandling\user_data2.txt"
with open(rel_path) as fh:
    data = fh.read()
print(data)
if fh.closed :
    print("file is closed")