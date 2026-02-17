import os 
### Renaming the file 
source_path = r"C:\Users\AURAGAM\Desktop\PythonTutorial\osModule\hello.txt"
destination_path = r"C:\Users\AURAGAM\Desktop\PythonTutorial\osModule\app.txt"
# ### use this for changing the files in the directory you want 
# os.rename(source_path  , destination_path)

### remove a file 
os.remove(destination_path)