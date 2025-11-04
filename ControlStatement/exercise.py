### Multi_way if statement
### Syntax
## if condition!1:
##         statement(s)
## elif condition!2:
##         statement(s)
## elif condition!3:
##         statement(s)
## else :
##     statement(s)
month: str = input("Enter your birth month: ")
if month == "January":
    print("Congratulations you were born in the first month of the year  ")
elif month == "Febuary":
    print("Congratulations you were born in the second month of the year ")
elif month == "March":
    print("Congratulations you were born in the third month of the year ")
elif month == "April":
    print("Congratulations you were born in the fourth month of the year")
elif month == "May":
    print("Congratulation you were born in the fifth month of the year")
elif month == "June":
    print("Congratulations you were born in the sixth month of the year")
elif month == "July":
    print("Congratulations you were born in the seventh month of the year")
elif month == "August":
    print("Congratulations you were born in the eigth month of the year")
elif month == "September":
    print("Congratulations you were born in the nineth month of the year")
elif month == "October":
    print("Congratulation you were born in the tenth month of the year  ")
elif month == "November":
    print("Congratulations you were born in the eleventh month of the year")
elif month == "December":
    print("Congratulation you were born in the last month of the year ")
else :
    print("Pls enter the name of the month \nThank you! ")
