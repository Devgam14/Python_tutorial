from pydal import DAL , Field
from datetime import date

##Creating Connection String to the database
connection = DAL("sqlite://nhs_db" , folder=r"ThirdPartyModules\pyDalMod\dbs")
print(connection)
##Creating table (emp_tbl) into database(nhs_db)