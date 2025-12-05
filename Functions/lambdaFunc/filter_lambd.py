salaries = [20000 , 80000 , 10000, 35000, 64000]
sal_obj = filter(lambda sal : sal > 30000 , salaries)
print(sal_obj)
up_sals = list(sal_obj)
print(up_sals)

user_names =  ["pEter", "paUl  ", "joHn  ", "JAmes  " , "MatT"]
name_obj = map(lambda name : name.title().strip() , user_names)
up_names = tuple(name_obj)
print(up_names)

name_obj = filter(lambda name : name.__contains__("a"), up_names)
print(list(name_obj))

name_obj2 = filter(lambda name : "a" in name , up_names)
print(list(name_obj2))
print("Hello world my geee mising you alot ")
