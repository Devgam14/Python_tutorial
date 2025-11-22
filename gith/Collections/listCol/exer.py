my_list = ["John" , "Paul", "Peter", "Annah", "James"]
new_list = []
for word in my_list:
    for char in word:
        if char == "a":
          new_list.append(word)
print(new_list)
number_of_char = 0
for word in new_list:
    for char in word:
        print(char)
        number_of_char += 1|""
print(number_of_char)
