from functools import reduce
l1 = [2,4,7,9,1,3]
sum_of_list1 = reduce(lambda a, b:a +b,l1)

def average (List : list) :
    avg = sum(List) / len(List)
    return round(avg)
  
  
l2 = ["abc", "xyz" , "def"]

max_of_list2 = reduce(lambda a, b:a if a>b else b, l2)
print(f"Sum of list1 : {sum_of_list1}")
print(f"Maximum of list2 : {max_of_list2}")

data = [
    {
        "id" : 1,
        "name" : "Paul",
        "age" : 20,
        "salary" : 2345.66
    },
    {
        "id" : 2,
        "name" : "Paul Jones",
        "age" : 34,
        "salary" : 20345.66
    },
    {
        "id" : 3,
        "name" : "Peter",
        "age" : 25,
        "salary" : 25645.66
    },
    {
        "id" : 4,
        "name" : "Hamayas",
        "age" : 30,
        "salary" : 25605.66
    },
    {
        "id" : 5,
        "name" : "Promise",
        "age" : 55,
        "salary" : 256005.66
    },
]

##list store
name_dictionary = dict()
name_list = []
age_list = []
sal_list = []


for dic in data :
    sal_list.append(dic["salary"])
    age_list.append(dic["age"])
    name_list.append(dic["name"])
sorted_list = sorted(name_list)
print(name_list)
for i , name in enumerate(sorted_list):
    name_dictionary[f"name{i}"]=name
print(f"Sum of ages {sum(age_list)}\nAverage age : {average(age_list)}")
sal_set = set(sal_list)
print(name_dictionary)
print(f"Average of salary = {round(sum(sal_set)/len(sal_set))}")
print(f"Min of salary = {min(sal_set)}")
print(f"Max of salary = {max(sal_set)}")