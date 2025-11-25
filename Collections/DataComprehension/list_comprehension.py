values = [23 , 45 , 12 , 98, 42, 68, 7,39]
print([x  + 20 for x in values])

## list comprehension to filter values greater than 20
print([x for x in values if x > 20])

print([ x for x in values if x % 2 == 0])
names = ["John" , "Paul", "Peter", "Paul", "James", "Jane", "Mary"]
print([y for y in names for z in y if z == "a"])
