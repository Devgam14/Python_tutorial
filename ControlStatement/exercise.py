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

month: str = input("Enter your birth month: ").lower()
if month == "january":
    print("Congratulations you were born in the first month of the year  ")
elif month == "febuary":
    print("Congratulations you were born in the second month of the year ")
elif month == "march":
    print("Congratulations you were born in the third month of the year ")
elif month == "april":
    print("Congratulations you were born in the fourth month of the year")
elif month == "may":
    print("Congratulation you were born in the fifth month of the year")
elif month == "june":
    print("Congratulations you were born in the sixth month of the year")
elif month == "july":
    print("Congratulations you were born in the seventh month of the year")
elif month == "august":
    print("Congratulations you were born in the eigth month of the year")
elif month == "september":
    print("Congratulations you were born in the nineth month of the year")
elif month == "october":
    print("Congratulation you were born in the tenth month of the year  ")
elif month == "november":
    print("Congratulations you were born in the eleventh month of the year")
elif month == "december":
    print("Congratulation you were born in the last month of the year ")
else :
    print("Pls enter the name of the month \nThank you! ")
