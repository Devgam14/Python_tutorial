print("WELCOME TO MY MONTH ACTIVITIES NOTE")
month: str = input("Enter the expected month: ").lower().strip()
print(month)
match month:
    case  "january":
        print("This is the month of january\nI travelled to my maternal home")
    case  "febuary":
        print("This is the month of febuary\nI moved to lagos")
    case  "march":
        print("This is the month of march\nI started going to mandilas ")
    case "april":
        print("This is the month of april\nI started learning react")
    case "may":
         print("This is the month of may\nI wrote my first react application")
    case  "june":
        print("This is the month of june\nI pushed the website to git-hub ")
    case "july":
        print("This is the month of July\nI started using my phone acode terminal to write react and nodejs applications ")
    case  "august":
        print("This is the month of august\nI stopped coding")
    case "september":
      print("This is the month of september\nI started coding again")
    case "october":
      print("This is the month of october\nI started learning python")
    case "november":
        print("This is the month of november\nI wrote some python programs like a calcukator and an atm simulator")
    case "december":
         print("This is the month of December\nI am going to start using nextjs full time ")
    case _:
        print("Pls enter the name of the month \nThank you! ")