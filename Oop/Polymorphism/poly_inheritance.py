class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Dogs Barks"
class Cat(Animal):
    def sound(self):
        return "Cat Meaoow"
class Bird(Animal):
    def sound(self):
     return "Bird Chirps"
 
dg = Dog()
bird = Bird()
cat = Cat()
animals = [dg , cat , bird]
for animal in animals:
    print(animal.sound())
## note method overloading is used to make a function do more than two things 
## method overiding is a way to overide a class methods 