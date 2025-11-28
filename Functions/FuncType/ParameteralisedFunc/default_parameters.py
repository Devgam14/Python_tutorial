#### Default Parameters
def message(user_name : str = "Paul Walker" , user_age : int = 22 ) -> str :
    return f"Hello {user_name} you are {user_age} years"

user_message = message("John Doe")
print(user_message)
user_message1 = message()
print(user_message)
user_message = message("Janet Joe" , 33)
print(user_message)
