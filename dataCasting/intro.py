"""
Data casting :: 
This is an act of converting data types to data types that they werent 
Casting Constructors 
1, int() ### from type to interger 
2, float() ### from any type to float (loosey conversion)
3, bool() ### from any Type to bool 
4, str() ### from any type  to str

"""
### from string to integer     
user_age : int = int(input("Enter your age >>>>> "))
print(user_age)
ival_type = type(user_age)
print(ival_type)

### float to integer 
emp_age : float = 23.98
emp_new_age = int(emp_age)
print(emp_new_age)
ival_type1 = type(emp_new_age)
print(ival_type1)

###bool to integer
is_Married = False
bool_conv = int(is_Married)
print(bool_conv)