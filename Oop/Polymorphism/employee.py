# from datetime import date

# class Person:
#     def __init__(self , name , age , dob):
#        self.age = age 
#        self.name = name 
#        self.dob = dob 
       
#     def __str__(self):
#         return f"Person name {self.name} , Person Age {self.age} , Person date of birth {self.dob}"
#     def get_info(self):
#         return f"Person Age {self.age} , Person Name {self.name} , Person Dob {self.dob}"
    
    
class Dog:
    def sound(self):
        return "Dogs Barks"
class Cat:
    def sound(self):
        return "Cat Meaoow"
class Bird:
    def sound(self):
     return "Bird Chirps"
# polymorphing function 
def animal_sound(animal):
    print(animal.sound())
dg = Dog()
animal_sound(dg)
bird = Bird()
animal_sound(bird)
cat = Cat()
animal_sound(cat)