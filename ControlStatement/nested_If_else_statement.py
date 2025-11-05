# Syntax of nested if else statement
# if statement == True:
#     if state == True:
#         print("True")
#     else:
#         print("false")
# else:
#     print("False 1")

username = input("Enter your username : ").strip().lower()
password = input("Enter your password : ").strip()
if username == "admin":
    if password == "passkey":
        print(f"Welcome Back {username}")
        print("You have full access")
    else:
        print("Invalid password")
else:
    print("Unrecognized User!!!!")