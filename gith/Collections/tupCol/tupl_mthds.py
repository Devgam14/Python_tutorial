user_names = ["Peter", "Paul", "John", "James","Peter", "Paul", "John", "James"]
users = tuple(user_names)
### note the count method returns the occurence of the particular value passed if in the tuple else it throws an error and it accepts only one argument
count_res = users.count("John")
### note the index methods uses start and stop values to find the indexs
index_res1 = users.index("John", 3)
index_res2 = users.index("John", 0, 4)

index_res = users.index("John")
print(index_res)
print(index_res1)
print(count_res)
print(users)