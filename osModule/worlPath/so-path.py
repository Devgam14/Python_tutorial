import os
my_path = r"C:\Users\AURAGAM\Desktop\PythonTutorial\osModule\workDir\create_dir.py"
## file name prints out file name 
base_pt = os.path.basename(my_path)
print(base_pt)

### folder name of path 
dir_pt = os.path.dirname(my_path)
print(dir_pt)

### file name spliting
dir_pt = os.path.splitext(my_path)
dirs_pt = os.path.split(my_path)
print(dirs_pt)
print(dir_pt)

print(os.path.exists(my_path)) ## returns boolean if conditions are matched 
print(os.path.isdir(my_path))
print(os.path.isfile(my_path))