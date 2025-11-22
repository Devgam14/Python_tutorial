### voting check 
age: int = int(input("Enter your age : "))
nationality: str = input("Enter your nationality : ").lower().strip()
if age >= 18:
    if nationality == "nigerian":
        print("Congratulations you are eligible to vote ")
    else:
        print("Dear user pls you are not eligible to vote because you are not a nigerian")
else :
    print(f"Sorry you are not eligible to vote\nyour age is {age} your age is lower than the required age")
    
