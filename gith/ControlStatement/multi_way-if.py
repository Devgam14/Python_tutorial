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

marks: int = int(input("Enter your marks: "))
if marks >= 90:
    print(" Congratulations You got an A grade")
elif marks >= 80:
    print(" Congratulations You got an B grade")
elif marks >= 70:
    print(" Congratulations You got an C grade")
elif marks >= 60:
    print("You got an D grade pls work hard next time ")
elif marks >= 50:
    print("You got an E grade, pls work harder next time")
else :
    print("Unfortunately you didnt pass see you next seemester")