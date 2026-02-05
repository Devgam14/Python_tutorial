from pydal import DAL , Field
from datetime import date

##Creating Connection String to the database
connection = DAL("sqlite://nhs_db" , folder=r"ThirdPartyModules\pyDalMod\dbs")
print(connection)
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

num_rows = connection(connection.My_Table.id).count()
print(f"The number of rows in the table is {num_rows}")