# ### A non void function returns data to the caller
# ### it must contain a "return" keyword

# def sum_num() : ## function body
#     fn = input("Enter a number ::: ")
#     sn = input("Enter a number :::: ")
#     return f"The sum of {fn} and {sn} is {int(fn) + int(sn)}" ### function body
    
# sum_num() ### function calling
# print(sum_num())

# def hello_msg():
#     name = "Paul"
#     return f"Hello,  {name} " ### function body
# msg = hello_msg()
# print(msg.upper())
# print(msg.lower())

def add_numbers():
    a = 12
    b = 34
    return a + b ### function body
res = add_numbers()
print(f"The sum of the numbers is : {res}") ### function Call
