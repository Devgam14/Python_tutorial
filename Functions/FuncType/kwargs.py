## note double asterisks means dictionary 
## note single asterisks means a tuple 
## note a kwarg returns a dictionary because of it you can use any dictionary method 
#key word Parameters

def my_friends(**kwargs) -> dict:
    return kwargs

myfriends = my_friends(one = "John", two = "Peter", three = "Paul" , four = "Mary")
print(myfriends)

my_friends = my_friends(eni = "Matt" , eji = "Jane" , eta = "Jssh")
print(my_friends)