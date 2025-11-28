### Arguments Parameters
## note a **arg returns a tuple because of it you can use any tuple method 

def my_friends(*args) -> tuple:
    return args[0 : 3] ### the returned statement for an *args func is a tuple so you can access the index 

my_friends_group = my_friends("john", "Peter", "Paul", "Mary", "Jane")
print(my_friends_group)
my_friend = my_friends("john", "Peter", "Paul", "Jane")
print(my_friend)

def user_info( *info) -> tuple :
    return info
data = user_info("John " , 23 ,  23456.9 , "Male" , "lagos")
print(data)
for data in data :
    print(data)