bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_data2.bin"
with open(bin_data, mode="rb") as fs:
    data = fs.read()
print(data)