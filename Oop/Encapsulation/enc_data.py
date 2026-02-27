### Access Specifier are these way 
## giving the instance variable  write the variables like these
## public name
## protected _name
## private __name this uses functions to set and get them 
class Employee:
    count = 0      ### Class variable
    ### Constructor
    
    ### passing the params for dynamic data 
    def __init__(self, id : int , name : str , age  : int, sal : float):
        ### Instance variables
        self.__id = id
        self.__name = name
        self.__age = age
        self.__salary = sal
        Employee.count += 1
        ## use the str method to allow printing and not meemory address
    def __str__(self):
        return f"Employee\nname {self.__name} \nId : {self.__id} \nAge : {self.__age} \nSalary : {self.__salary}"
               
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_salary(self):
        return self.__salary
    
    
    def set_name(self , name : str):
        if name == " " or type(name) == int:
            raise ValueError
        self.__name = name
        
    def set_id(self , id):
        if id == " " or type(id) == int :
            raise ValueError
        self.__id = id
    def set_salary(self , salary):
        if salary == " " or type(salary) == int :
            raise ValueError
        self.__salary = salary
    def set_age(self , age):
        if age == " " or type(age) == str :
            raise ValueError
        self.__age = age
    # instance method 
    def emp_info(self):
        return f"Employee name {self.name} \n Id : {self.id} \n Age : {self.age} \n Salary : {self.salary}"
    
user = Employee( 2, "gam", 30 , 3002 )
print(user)

### getting the data 
### you can use the dot notation to get the attribute of the class 
# print(user.name, user.age , user.salary , user.id)
### note that data can be dynamic 
### setting the value
val = user.get_name()
print("line 62")
print(val)
val1 = user.set_name("goiu")
val2 = user.get_name()
print(val2)



# user.get_name()

# print(user)
# engineer = Employee(4 , "mamuel", 38 , 332.02 )
# print(engineer)
# teacher = Employee(8 , "hilma", 40 , 30078.4 )
# print(teacher)

