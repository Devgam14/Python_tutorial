try :
    bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user_d.bin"
    with open(bin_data, mode="r") as fs:
        ### always remember to use the wb in the mode 
        data = fs.write(b"finalyy working with files in python")
except FileNotFoundError:
    print("Nna biko ")
finally:
    print("File read")