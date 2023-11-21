class Person:
    
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.height = 10
        self.weight = 20
    
    def get_age(self, current_year):
        """
        Returns the age of person given the current_year.
        current_year is an integer.
        """
        year = self.dob.split('-')[-1]
        age = current_year - int(year)
        return age
    
    def introduction(self):
        """
        Returns the a full introduction of the instance of Person.
        """
        return "Hi my name is {} and I am {} years old.".format(self.name, self.get_age(2023))

person1 = Person('Fatima Usman', '12-01-2023')
person2 = Person('Ahmad Usman', '12-01-2021')

print(person1.name)
print(person1.dob)
print(person1.get_age(2050))
print(person1.introduction())
print(person2.name)
print(person2.dob)
print(person2.get_age(2050))
print(person2.introduction())

class Animal:

    def __init__(self, group, name, sound):
        self.group = group
        self.name = name
        self.sound = sound
        self.energy_level = 100
    
    def get_info(self):
        return "Hi my name is {}, I am a {} and I make a {} sound".format(self.name, self.group, self.sound)
    
    def feed(self, food_quantity):
        self.energy_level += (0.1*food_quantity)


class Dog(Animal):

    def bark(self):
        if self.energy_level > 30:
            self.energy_level -= (0.1*self.energy_level)
            return (self.sound+" ") * 6
        return "I am too hungry for anything right now"

class Cat(Animal):

    def meow(self):
        if self.energy_level > 50:
            self.energy_level -= (0.05*self.energy_level)
            return (self.sound+" ") * 6
        return "I am too hungry for anything right now"
    
dog1 = Dog('Canine', 'Malone', 'Woo')
cat1 = Cat('Cat', 'Tiger', 'Meow')
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.meow())
print(cat1.energy_level)
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.energy_level)
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.bark())
print(dog1.energy_level)
print(dog1.get_info())

print("\n\n\n\n\n")

p1 = Person('Habu', '12-01-1985')
p2 = Person('Musa', '12-01-1990')

print(p1.get_age(2023))
print(p2.get_age(2023))