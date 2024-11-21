# Assignment 1: Design Your Own Class! 🏗️
""" class Smartphones:
    
    def __init__(self, name, model, price):
        self.name = name
        self.model = model
        self.__price = price
        
    def get_price(self):
        return self.__price
    
    def price_increment(self, new_price):
        self.__price += new_price
        return (f"The new price of {self.name} {self.model} is ${self.__price}")


s23 = Smartphones('Samsung', 's23', 250 )

print(f'The price of the smartphone is ${s23.get_price()}')

print(s23.price_increment(23))


class Laptop(Smartphones):
    
    def get_price(self):
        return super().get_price()
    
    def price_increment(self, new_price):
        return super().price_increment(new_price)
    
    def discount(self, discount_rate):
        current_price = self.get_price()
        final_price = current_price - (current_price * discount_rate / 100)
        return final_price
        
        
        
omen = Laptop('HP', 'omen', 750 )

print(f'The price of the laptop is ${omen.get_price()}')

print(omen.price_increment(100))

print(omen.discount(50))
 """
 
 
# Activity 2: Polymorphism Challenge! 🎭
class Animal:
    def speak(self):
        return "All animal can speak"

class Dog:
    def speak(self):
        return "Dog Woof!"
    
class Snake:
    def speak(self):
        return "Snake hiss"

class Cat:
    def speak(self):
        return "Cat Meow!"
    

animals = [Animal(), Dog(), Snake(), Cat()]

for animal in animals:
    print(animal.speak())
