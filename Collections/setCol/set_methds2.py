users_names1 = {"Paul", 'Peter', "James", 'John', 'Chloe', "Matt"}
users_names2 = {"Paul", "Ruth", "James", 'Matt'}

new_users = users_names1.union(users_names2)
print(new_users)
### note instead of using union method you can use | symbol
print(users_names1 | users_names2)

intr_sets = users_names1.intersection(users_names2)
print(intr_sets)
### note instead of using intersection methd use the ampersand symbol &
print(users_names1 & users_names2)

intr_sets = users_names1.difference(users_names2)
print(intr_sets)
### note instead of using difference methd use the minus symbol -
print(users_names1 - users_names2)

intr_sets = users_names1.symmetric_difference(users_names2)
print(intr_sets)
### note instead of using symmetric_difference methd use the chevron symbol ^
print(users_names1 ^ users_names2)
