from io import UnsupportedOperation

try :
    ## remeber that you ca just pass in the mode with the placeholder 
    with open(r"C:\Users\AURAGAM\Desktop\PythonTutorial\FileHandling\user.txt" , "w") as fs :
        text = fs.read(34)
        print(text)
except FileNotFoundError:
    print("Your file is missing, check your directory ")
except UnsupportedOperation:
    print("Check your mode")
finally :
    print("File closed successfully")