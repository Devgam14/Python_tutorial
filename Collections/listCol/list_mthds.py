animals = ["Dog", "Cat", "Hen", "Goat","Cow","Parrot","Lion","Wolf","Tiger"]
animals.append("Owl")
animals.append(["Fowl", "Rat"])
print(animals)
### note append method does not return anything 

animals.insert(1 , "Camel")
pop_items = animals.pop()
pop_item1 = animals.pop(4)
## note that pop method removes the last datatype or lat thing  when nothing is provided when no index is provided

animals.remove("Tiger")
### note if no value is provided it removes nothing and throws an error if value is not found it throws an  error 
animals.extend(['Snakes, "Pig'])
### note that it is only iterables that are being used in this extend method else it throws an error 
print(animals)
animals.sort(reverse=True)
### note this sorts a ;ist
animals.clear()
### note this removes everything from a list
print(pop_items)
print(animals)