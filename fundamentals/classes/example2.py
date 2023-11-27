class Person:
    def __init__(self, name, height, age, weight):
        self.name = name
        self.height = height
        self.age = age
        self.weight = weight
    
    def get(self):
        """
        Return basic information about an instance of Person
        """
        print("Hi my name is {}, I am {} years old I currently weigh {}kg and I am {}m tall".format(self.name, self.age, self.weight, self.height))

x = Person("Kabir", 2.1, 19, 10.6)
y = Person("Zainab", 10.2, 12, 45.7)

x.get()
y.get()

