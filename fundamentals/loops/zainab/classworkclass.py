class animal:
    def __init__(self,type,name,color,sound,weight):
        self.type = type
        self.name = name
        self.color = color
        self.sound = sound
        self.weight = weight

    def get(self):
        print("This {} is a {} that has a {} color and {} when it makes a sound and also weight {}kg".format(self.type, self.name, self.color, self.sound, self.weight))

xx = animal("snake", "cobra", "green", "hiss", 23.5)
xx.get()

class books:
    def __init__(self, title, author, publisher, year):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.stock = 0
        self.sold = 0
        self.purchases = 0

    def setprice(self, price):
        self.price = price
        print("the prices of {} has been set to be {}$".format(self.title, self.price))

    def addstock(self, quantity):
        self.stock += quantity
        print("we have {} more copies of {} added to stock".format(quantity, self.title))

    def sell(self, quantity):
        if self.stock == 0:
            print("the book {} is out of stock".format(self.title))
        elif self.stock > quantity:
            self.sold += quantity
            self.stock -= quantity
            self.purchases += (quantity*self.price)
            print("{} copies of of the book {} has been sold successfully".format(quantity, self.title))
        else:
            print("we dont have up to {} copies of {} in stock".format(quantity, self.title))

    def thereport(self):
        print("__"*len(self.title))
        print("title:", self.title)
        print("stock:", self.stock)
        print("sold:", self.sold)
        print("price:",self.price)
        print("total:", self.purchases)
        print("__"*len(self.title))


A = books("wutheing heights", "emily bronte", "i dont know", 2004)
B = books("the great gatsby", "scott fitzgerald", "i dont know", 2011)
C = books("things have fall apart", "wole soyinka", "i dont know", 2014)

A.setprice(2000)
B.setprice(5000)
C.setprice(3000)
books.addstock(25)
books.sell(30)
books.sell(10)
A.report()
B.report()
C.report()

