message = "Congratulation"
###accessing strings items or character
print(message[3])
print(message[7])
print(message[-3])

###counting items in strings or characters
print(len(message))

# ## string mutation
# res = message[3] = "b"
# print(res)
### Note the code above would throw an error strings are immutable

print(sorted("ACCOUNT" , reverse=False)) ### note the sorted method sorts characters alphabeticallly 

### String Methods
user_name = "pAul pETer"
up_case = user_name.upper()
print(up_case)
low_case = user_name.lower()
print(low_case)
tit_case = user_name.title()
print(tit_case)
cap_case = user_name.capitalize()
print(cap_case)
swap_case = user_name.swapcase()
print(swap_case)

data = "    Thank you so much       "
print(data)
print(len(data))
srt_data = data.strip()### strip() remove unwanted white spaces froma string cos sometimes can be counted as strings
print(len(srt_data))
print(srt_data)


r_srt_data = data.rstrip()### right striping 
print(len(r_srt_data))

print()

l_srt_data = data.lstrip() ### left striping 
print(len(l_srt_data))

find_res = message.find("lat" , 3 , 7)### try to find if a particular substring exist in n a range of indexes
print(find_res)

count_res = message.count("a", 5 , 8)### count how many appearance a particular sub string appear in a range of indexes
print(count_res)

my_music = "laho.mp3"
start_with = my_music.startswith("la")##Checks if a strings starts wtth a particular character or substring
print(start_with)

end_with = my_music.endswith("mp3")##Checks if a strings ends wtth a particular character or substring
print(end_with)

encode_str = message.encode(encoding="utf-32")
print(encode_str)

print(message.split("/" , 5))
