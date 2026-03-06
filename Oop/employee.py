### Access Specifier are these way 
## giving the instance variable  write the variables like these
## public name
## protected _name
## private __name
class Employee:
    count = 0      ### Class variable
    ### Constructor
    
    ### passing the params for dynamic data 
    def __init__(self, id : int , name : str , age  : int, sal : float):
        ### Instance variables
        self.id = id or 2
        self.name = name
        self.age = age
        self.salary = sal
        Employee.count += 1
        ## use the str method to allow printing and not meemory address
    def __str__(self):
        return f"Employee\nname {self.name} \nId : {self.id} \nAge : {self.age} \nSalary : {self.salary}"
               
    # instance method 
    def emp_info(self):
        return f"Employee name {self.name} \n Id : {self.id} \n Age : {self.age} \n Salary : {self.salary}"
    
user = Employee( 2, "gam", 30 , 3002 )
user1 = Employee( 5, "dapo", 3000 , 30020000 )
print(user.emp_info())
print(user1.emp_info())
### getting the data 
### you can use the dot notation to get the attribute of the class 
# print(user.name, user.age , user.salary , user.id)
# ### note that data can be dynamic 
# ### setting the value

# user.name = "Amina"
# user.id = 5
# user.salary = 20000.000

# print(user)
# engineer = Employee(4 , "mamuel", 38 , 332.02 )
# print(engineer)
# teacher = Employee(8 , "hilma", 40 , 30078.4 )
# print(teacher)

