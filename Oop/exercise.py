from dataclasses import dataclass
### Access Specifier are these way 
## giving the instance variable  write the variables like these
## public name
## protected _name
## private __name
@dataclass()
class Laptop:
    model : str
    price : float
    ram : int
    ssd : float
    brand : str 
    def __str__(self):
        return f"My laptop details are below : \n \n Brand :{self.brand} \n Model :{self.model}\n Price :#{self.price}\n \n Storage details : \n \n  RAM: {self.ram}gb  \n  SSD: {self.ssd}gb"

my_pc = Laptop("X230", 200_000 , 8 , 128.3 , "Lenovo")
print(my_pc)