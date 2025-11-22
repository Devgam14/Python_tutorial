### using ==== []
my_items : list = ["Bag", ["dog", "cat", "goat"], "Belt", 23, 56.98, True , range(0,6)]
print(my_items[1][0])
my_items[1][2] = "hen"
print(my_items)

### Using constructor
my_str = list("Congrats")
print(my_str)

my_values = list()
my_values.append(23)
my_values.append(253)
my_values.append(563)
my_values.append(2093)
my_values.append(1223)
print(my_values)
### note list can be nested there can list of list in list of list in list of list 
###note the append method is used to add 