"""class Animal():
    def sound(self):
        print("Animal Makes sound")

class Dog(Animal):
    def sound(self):
        print("Bark...")

class Cat(Animal):
    def sound(self):
        print("Meow...")

animals = [Dog(), Cat()]
for a in animals:
    a.sound()"""  

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    pass

a = Animal()