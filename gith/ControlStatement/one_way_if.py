# ## One-way if statement
# ## Syntax
# # if condition:
# #       statement(s)
if False:
    print("This is a one-way if statement ")
    print("The condition is true, so this block executes. ")
    print("Inside the if block, you can have multiple statements ")

if True:
    pass ## This block does nothing but it is a valid syntax 
### Example of one-way if Statement 
## Check if a number is positive 
number= input("Enter a number: ")
number: int = int(number) # Convert Input to interger 
if number > 0:
    print(f"The number {number} is positive. ")
    
voters_age: int = int(input("Enter your age: "))
if voters_age >= 18 :
    print("You are eligible to vote. ")
