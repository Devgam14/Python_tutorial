### note set changes regullarly it is not arranged like lists it changes so trhe speak the arrangement is dynamic

users = set()
users.add("John")
users.add("Peter")
users.add("James")
users.add("Ruth")
users.add("Math")
users.add("James")
users.add("Ruth")
print(users)

pop_ele = users.pop()
users.update(["kemi", "Chioma", "Tracy"])
print(pop_ele)
### note the update method collects and iterable and converts them to a set
copy_users = users.copy()
print(copy_users)

### note the remove method throws an error when the element to be removed is not found while the discard mnethod does not throw an error 
###users.remove("James")
users.remove("John")
users.discard("jjjjjjjjjjjjjjjjjjj")