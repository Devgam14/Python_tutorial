
#Syntax
# match new:
#     case "monday":
#         print("this is the first day of the week ")
#     case "tuesday":
#         print("This is the second day of the week")
#     case "wednesday":
#         print("This si the third day of the week")
#     case "thursday":
#         print("this is the fourth day of the week")
#     case _:
#         print("Pls enter the name of the month \nThank you! ")
    

new: str  =  input("Enter the day of the week below :\n").strip().lower()
match new:
    case "monday":
        print("this is the first day of the week ")
    case "tuesday":
        print("This is the second day of the week")
    case "wednesday":
        print("This si the third day of the week")
    case "thursday":
        print("this is the fourth day of the week")
    case "friday":
        print("this is the fifth day of the week")
    case "saturday":
        print("This is the sixth day of the week")
    case "sunday":
        print("this is the seventh day of the week")
    case _:
        print("Pls enter the name of the week \nThank you! ")
### THis is just like switch in javascriptn   
