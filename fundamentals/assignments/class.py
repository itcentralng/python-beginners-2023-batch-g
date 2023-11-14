# Q1. 
# Write a class for books with the following info: title, author, publisher, year.

# Q2.
# Using Q1 above, add a method for setting the selling price of the book
# Add a method for selling books
# Add a way of keeping track of the number of books sold
# Add a way of keeping track of the number of books in stock

class Book:
    def __init__(self, title, author, publisher, year) -> None:
        self.title = title
        self.author = author
        self.publisher = publisher
        self.year = year
        self.sold = 0
        self.stock = 0
        self.purchases = 0
    
    def addStock(self, quantity):
        self.stock += quantity
        print("{} more copies of {} added to stock!".format(quantity, self.title))
    
    def setPrice(self, price):
        self.price = price
        print("The price of {} has been set to ${}".format(self.title, self.price))
    
    def sell(self, quantity):
        if self.stock == 0:
            print("{} is out of stock!!!".format(self.title))
        elif self.stock > quantity:
            self.sold += quantity
            self.stock -= quantity
            self.purchases += (quantity*self.price)
            print("{} copies of {} sold successfully!".format(quantity, self.title))
        else:
            print("We don't have up to {} copies of {} in stock!".format(quantity, self.title))
    
    def report(self):
        print("-"*len(self.title))
        print('Title:\n', self.title)
        print('Stock:', self.stock)
        print('Price:', self.price)
        print('Sold:', self.sold)
        print('Total:', self.purchases)
        print("-"*len(self.title))


book = Book('Harry Potter and the Prisoner of Azkaban', 'J.K Rowling', 'Random House',  '2010')
book2 = Book('Harry Potter and the Deadly Hallows', 'J.K Rowling', 'Random House',  '2012')
book3 = Book('12 Rules for Life', 'Jordan B. Petterson', 'Random House',  '2013')
book4 = Book('Rich Dad Poor Dad', 'Robert Kiwosaki', 'Random House',  '2014')

book.setPrice(500)
book2.setPrice(200)
book3.setPrice(1500)
book4.setPrice(2000)
book.addStock(35)
book.sell(20)
book.sell(10)
book.report()
book2.report()
book3.report()
book4.report()

# Q3.
# Create a class to manage a shop with the following information:
# - Shop name
# - Items in the shop:
#       - name, price, stock
#       - item(s) should be able to be added
#       - stock should be able to be updated
#       - price should be ablt to be updated
# - Perform Transaction:
#       - items should be sold
#       - receipts should be given
# - Track transactions:
#       - given a transactionId, return the transaction
# - Track total sales
#       - units sold
#       - revenue