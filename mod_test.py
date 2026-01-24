## Importing everything 
# import package.sums_nums as string_formater
from package.sums_nums import *
## Importing specific things 
from package.sums_nums import sum_nums , name_formater , User , user_name as Username
namer = name_formater("gam")
### Note when using the asterisk method it means all everything inside the file 
### This brings about the importance of documenting a function
print(sum_nums([23,24,35,78,45,63,72,81,90,27]))
print(sum_nums([]))