data = r"FileHandling\users.txt"
### Always remember to add the a in the mode inside the open 
with open(data , mode="a") as fs:
    fs.writelines(["Hello \n", "Is been a while bro \n" , "working on a telco program \n"])