salaries = [23456 , 98765 , 87034 , 26734 , 93561]
sal_obj = map(lambda sal : sal + (sal * 0.1) , salaries)
print(sal_obj)
up_sals = list(sal_obj)
print(up_sals)

user_names =  ["pEter", "paUl  ", "joHn  ", "JAmes  " , "MatT"]
name_obj = map(lambda name : name.title().strip() , user_names)
up_names = tuple(name_obj)
print(up_names)