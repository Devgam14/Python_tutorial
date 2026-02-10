from prettytable import PrettyTable
from faker import Faker
## Initializing librairies 
faker_lib = Faker("en_NG")
table = PrettyTable([ "ID" ,"Firstname", "Lastname" , "Age" , "Date of birth" , "Salary"])
currency = faker_lib.currency_symbol(code="NGN")
lists = []
listStore = []
salary_list = []
table.align = "l"

for _ in range(1,10) :
    ## generating fake details
    first_name = faker_lib.first_name()
    last_name = faker_lib.last_name()
    age = faker_lib.random_int(min=18 , max=60)
    dob= faker_lib.date_of_birth().strftime("%d/%m/%Y")
    salary = faker_lib.random_int(min=3000, max=1000090)
    id = faker_lib.random_int(min=1, max=1000)
    salary_list.append(salary)
    lists.append([ id , first_name , last_name , age , dob , f"{currency}{salary}"])
    listStore.append(lists[0])
    lists = []

average = round(sum(salary_list) / len(salary_list))
table.add_rows(listStore)
table.add_row(["Min", f"{currency}{min(salary_list)}" , "" , "" , "" , ""])
table.add_row(["Max", f"{currency}{max(salary_list)}" , "" , "" , "" , "" ])
table.add_row(["Avg salary", f"{currency}{average}" , "" , "" , "" , "" ])

print(table)