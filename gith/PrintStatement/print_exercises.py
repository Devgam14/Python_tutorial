##### Employee Profile 
emp_name : str = "gamaliel"
emp_age : int = 25
is_hired : bool = True
emp_weight : float = 75.87

#### normal concat method 
###print("Employee Data = Name : " + emp_name + "Age : " + emp_age1 + "employee was hired : " + is_hired + "he weighs : " + emp_weight)

#### f-string method 
print(f"Employee's Data = Name : {emp_name} Age: {emp_age}, is employee hired : {is_hired}, employee's weight is : {emp_weight}")

#### string format
print("Employee's Data = Name : {0} Age: {1}, is employee hired : {2}, employee's weight is : {3} ".format(emp_name,emp_age,is_hired,emp_weight))

#### old_f-string method 
print("Employee's Data = Name : %s Age: %i, is employee hired : %d employee's weight is : %f " %(emp_name,emp_age,is_hired, emp_weight))


#### these are the methods of printing in python  

print(f"employees age is {emp_age} employees's weight is {emp_weight} so to speak we say that: {emp_name} is working and he is {emp_age} old is he hired ? {is_hired}")
