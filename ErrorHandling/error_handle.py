### try except finally

try :
    number = "34"
    number2 = 23
    result = number + number2
    print(result)
except ValueError:
    print("Please check your Input !!!!!!")
except TypeError as typErr:
    print("Check your dataType ", typErr.__doc__)
    