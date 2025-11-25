countries : dict = {"ng" : "Nigeria", "gh" : "Ghana", "ml" : "Mali", "bn" :"Benin", "tg" : "Togo"}
print(countries.update({"ci" : "Cote d'Ivoire" , "sn" : "Senegal"}))
### this is the add method it is used to upadte a dict or to add new values
new_dict = countries.copy()
print(new_dict)
### the copy method returns the value of the the item if found else it returns the default
get_item = new_dict.get("ng", "Not Found") #Returns "Nigeria"
print(get_item)
dict_items = new_dict.items()
print(dict_items)
### it removes the value and stores it in a variable for access If the key is not found, return the default if given; otherwise, raise a KeyError.
pop_value = new_dict.pop("bn" , None) ### Removes "Benin" if it exist
### this returns the keys in a set like format
print(pop_value)
all_keys = new_dict.keys() ### returns all the keys in the dictionary
print(all_keys)
all_values = new_dict.values() ### returns al the values in the dictionary 
print(all_values)
pop_it = new_dict.popitem() ### Removes and returns the last key-value pair
print(pop_it)
print(new_dict.setdefault("tg", "Togo")) ## does not change anything since "tg" exists
print(dict_items)
user_items = {}
new_user = user_items.fromkeys(["us", "uk", "fr"], "Unknown")
## creates new keys with "Unknown as value"
print(new_user)
print("new dicts", new_dict)
print(get_item)
# new_dict.clear() ### clears everything in the dictionary 
new_dict["ml"] = "Malaysia"
print(new_dict)
print(new_dict["gh"])

for key, value in new_dict.items():
    print(f"{key} , {value}")
for key , value in new_dict.items():
    print(f" value {key}")
