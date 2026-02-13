bin_data = r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\bin_writelines.bin"
with open(bin_data, mode="wb") as fs:
    ## make sure to use wb
    fs.writelines([b'12\n',
                   b'34\n',
                   b'56 \n',
                   b'89 \n',
                   b'134 '])
