bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_data2.bin"
with open(bin_data, mode="rb") as fs:
    ## always remember that you must pass value for the about of byte
    data = fs.readline()
print(data)
