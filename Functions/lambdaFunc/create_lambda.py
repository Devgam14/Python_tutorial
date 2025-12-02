

### void lambda function
user_info = lambda name , age : print(f"My name is {name} , My age is {age}")
user_info("John", 30)

### non void lambda function functions that return something 
user_data = lambda name , age : f"My name is {name} , My age is {age}"
data_res = user_data("John" , 50)
print(data_res)