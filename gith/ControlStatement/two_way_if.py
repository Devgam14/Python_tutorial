### Two-way if statement
### Syntax
## if condition:
##       statement(s) for true condition
## else:
##       statement(s) for false condition

### Example of a two-way if statement 
voters_age: int = int( input("Enter your age: "))
if voters_age >= 18 :
    print("Congratulations! you are eligible to vote ")
else :
    print("Unfortunately, you are not eligible to vote ")

### Script to check if a number is even or odd 
number : int = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number {number } is an even number ")
else:
    print(f"The number {number} is an odd number")