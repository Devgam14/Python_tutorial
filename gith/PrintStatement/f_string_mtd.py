person_name = "James"
user_name : int = "Peter"
user_age : int  = 23
person_age : int = "23"
person_salary : float = 12345.98
PERSON_CONST = "change"
#####f-string Concat Approach 
print(f"My name is {person_name.upper()}, I am {user_age:.02f} years old")
print(f"User Name is ::::: {user_name.title()} His salary is :::::  {person_salary:.0e}")
print(f"person name is {person_name.lower()}")

####second examples 
users_name = "John Doe"
other_name = "Matt"
full_name = f"My name is {users_name} , My other name is {other_name}"
print(full_name)

my_id = "12233";
user_location = "Lagos"
users_age = "34"

print(f"Id :::: {my_id} , My location ::::  {user_location} , age :::: {users_age}")
