class Person: ### can be called the super class or parent class 
    def __init__(self, id: int, name: str, age: int):
        self._id = id
        self._name = name
        self._age = age
    def __str__(self):
        return f"Employee\nName: {self._name} \nId: {self._id} \nAge: {self._age}"
    def emp_info(self):
        return f"Employee name: {self._name}\nId: {self._id}\nAge: {self._age}"
    
class Employee(Person): ### child class
        def __init__(self , id , name , age , salary : float , post : str):
            super().__init__(id , name , age)
            self._salary = salary 
            self._post = post
        def get_info1(self) :
            return f"name : {self._name} , age : {self._age} , salary : {self._salary}"
        def get_info2(self) :
            return f"position : {self._post} , salary : {self._salary}"
            
teacher = Employee(23 , "paul_scholes" , 34 , 234.56 , "director")
print(teacher)
print(teacher.get_info1())
print(teacher.get_info2())
