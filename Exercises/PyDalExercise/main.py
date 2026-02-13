from pydal import DAL , Field
from faker import Faker
from datetime import date
from prettytable import PrettyTable

faker_mod = Faker("en_NG")
p_table = PrettyTable(["Names", "Age" , "DOB" , "Gender" , "Salary" , "Email" , "Phone_Numbers"])
store1 = []
store2 = []
country_code = faker_mod.currency_symbol(code="NGN")
##Creating Connection String to the database
connection = DAL("sqlite://nhs_db" , folder=r"Exercises\PyDalExercise\dbs")
##Creating table (emp_tbl) into database(nhs_db)
connection.define_table("My_Table",
Field("Names" , type="string" , length=50 , required=True),
Field("Age" , type="integer" , required=True),
Field("DOB" , type="date" , required=True),
Field("Gender" , type="string" , required=True, length=10, default="MALE"),
Field("Salary" , type="decimal(10,2)" ),
Field("Email" , type="string" , required=True, length=50, unique=True),
Field("Phone" , type="string" , required=True, length=15, unique=True),
)
if connection :
    print("Connected Successfully")


connection.My_Table.truncate()
connection.commit()
for _ in range(1,30):
    year = int(faker_mod.year())
    month = int(faker_mod.month())
    day = faker_mod.random_int(min=1 , max=28)
    salary = faker_mod.pyfloat(positive=True , left_digits=6 , right_digits=2 ,min_value=10000 , max_value=1_000_000)
    connection.My_Table.insert(Names=f"{faker_mod.name_male()}" , Age=f"{faker_mod.random_int(min=19 , max=60)}" , DOB=date(int(year),month ,int(day)) , Gender=f"{faker_mod.random_element(elements=('MALE' , 'FEMALE'))}" , Salary=float(salary), Email=f"{faker_mod.email()}" , Phone=f"{str(faker_mod.phone_number())}")
rows = connection(connection.My_Table).select()
for row in rows:
    store1.append([row["Names"], row['Age'] , row["DOB"], row["Gender"] , f"{country_code}{row["Salary"]}" , row["Email"] , row["Phone"]])
    store2.append(store1[0])
    store1 = []
if connection:
    connection.close()
p_table.add_rows(store2)
p_table.align = "l"
print(p_table)
data_file = r"C:\Users\AURAGAM\Desktop\PythonTutorial\Exercises\pty.py"
with open(data_file , mode="a") as fs :
    fs.write(store1)
