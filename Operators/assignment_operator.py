#Assignment Ops
# -Equals  (=)
name : str = "John"
age : int = 45

#   -Augumented assignment ops
#       -plusEqual (==)
user_name   = " Paul "
user_name  += " Peter "     ### user_name  = user_name + "Peter"
user_name  +=   " John "     ### user_name  = user_name + "John"
print(user_name)

user_name = user_name + " Matt"
print(user_name)

user_age : int = 12
user_age += 10    ## user_age = user_age + 10
user_age += 10
print(user_age)
user_age = user_age + 50
print(user_age)


#   minusEquals
debt: float = 120_000_000
debt -= 20_000_000
debt -= 100_000_000
print(debt)


##   multi 
num = 3
num *= 5
print(num)

name = "Peee   "
name *= 3
print(name)

### MOdulus
val = 53
val %= 15
val %= 5
print(val)

### Expontential
val2 =4
val2 **= 2
val2 **= 5
print(val2)

###3 
## division and division floor // it truncates it doesnt round up 
value2 = 4
value2 /= 3
print(value2)


value1 = 4
value1 //= 3
print(value1)

