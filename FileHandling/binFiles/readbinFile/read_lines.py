bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_data2.bin"
with open(bin_data, mode="rb") as fs:
    data = fs.readlines()[2]
    data2 = fs.readlines()
print(data)
print(data2)