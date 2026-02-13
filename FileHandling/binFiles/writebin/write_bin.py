bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_d2.bin"
with open(bin_data, mode="wb") as fs:
    ### always remember to use the wb in the mode 
    data = fs.write(b"finalyy working with files in python")
print(data)