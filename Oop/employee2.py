from dataclasses import dataclass



### Access Specifier are these way 
## giving the instance variable  write the variables like these
## public name
## protected _name
## private __name

### use dataclases to create simple classes 
### the init is the constreuctor 
### you can use repr when using dataclases and you dont need the __str__ method anymore it only works when repr is true  and only when there is an overridden function inside the class
@dataclass(init=True , repr=False)
class Person():
    id : int
    name : str
    age : int
    sal : float
    def __repr__(self):
        return f"Employee\nname {self.name} \nId : {self.id} \nAge : {self.age} \nSalary : {self.sal}"
        
    # def __str__(self):
    #     return f"Employee\nname {self.name} \nId : {self.id} \nAge : {self.age} \nSalary : {self.sal}"
    
army_man = Person(2 , "kabuk", 34 , 9000.46)
print(army_man)
nurse = Person(20 , "chidinma", 24 , 19000.46)
print(nurse)
police_man = Person(12 , "Yusuf", 54 , 6000.46)
print(police_man)