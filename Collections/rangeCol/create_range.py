
range_obj = range(5) ## this line generate value from 0 to 4
print(range_obj)

for value in range_obj: ## looping the range object
    print(value , end=" , ")
print()
numbers = range(2 , 11) ## generate 2 to 10
for number in numbers:
    print(number , end=" ")
print()

data = range(10, 100, 10)## generate from 10 to 90 in the step of 10 
for dt in data:
    print(dt , end=" ")
enum_obj = enumerate(data)
print()
print(list(enum_obj))

print()