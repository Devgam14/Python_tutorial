from prettytable import PrettyTable
from faker import Faker
table = PrettyTable()
fk = Faker()
lister = []
list_of_list = []

for _ in range(1,5):
        name = fk.name()
        country = fk.country()
        country_code = fk.country_calling_code()
        
        lister.append([name , country])
        list_of_list.append(lister)

table.add_rows(list_of_list)
print(table)