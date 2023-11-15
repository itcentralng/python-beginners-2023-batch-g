# # Q1. 
# # Write a class for books with the following info: title, author, publisher, year.

# # Q2.
# # Using Q1 above, add a method for setting the selling price of the book
# # Add a method for selling books
# # Add a way of keeping track of the number of books sold
# # Add a way of keeping track of the number of books in stock

# class Book:
#     def __init__(self, title, author, publisher, year) -> None:
#         self.title = title
#         self.author = author
#         self.publisher = publisher
#         self.year = year
#         self.sold = 0
#         self.stock = 0
#         self.purchases = 0
    
#     def addStock(self, quantity):
#         self.stock += quantity
#         print("{} more copies of {} added to stock!".format(quantity, self.title))
    
#     def setPrice(self, price):
#         self.price = price
#         print("The price of {} has been set to ${}".format(self.title, self.price))
    
#     def sell(self, quantity):
#         if self.stock == 0:
#             print("{} is out of stock!!!".format(self.title))
#         elif self.stock > quantity:
#             self.sold += quantity
#             self.stock -= quantity
#             self.purchases += (quantity*self.price)
#             print("{} copies of {} sold successfully!".format(quantity, self.title))
#         else:
#             print("We don't have up to {} copies of {} in stock!".format(quantity, self.title))
    
#     def report(self):
#         print("-"*len(self.title))
#         print('Title:\n', self.title)
#         print('Stock:', self.stock)
#         print('Price:', self.price)
#         print('Sold:', self.sold)
#         print('Total:', self.purchases)
#         print("-"*len(self.title))


# book = Book('Harry Potter and the Prisoner of Azkaban', 'J.K Rowling', 'Random House',  '2010')
# book2 = Book('Harry Potter and the Deadly Hallows', 'J.K Rowling', 'Random House',  '2012')
# book3 = Book('12 Rules for Life', 'Jordan B. Petterson', 'Random House',  '2013')
# book4 = Book('Rich Dad Poor Dad', 'Robert Kiwosaki', 'Random House',  '2014')

# book.setPrice(500)
# book2.setPrice(200)
# book3.setPrice(1500)
# book4.setPrice(2000)
# book.addStock(35)
# book.sell(20)
# book.sell(10)
# book.report()
# book2.report()
# book3.report()
# book4.report()

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

class Shop:
    def __init__(self, name):
        self.name = name
        self.items = {}
        self.transactions = {}
    
    def add_item(self, name, price, stock):
        """
        Add a new item to Shop

        `name`: name of the item to add
        
        `price`: price for the item

        `stock`: avaiable units in Shop
        """
        self.items[name] = {'price':price, 'stock':stock}
        print('{} units of {} added to shop successfully!'.format(stock, name))
    
    def update_stock(self, item_name, units):
        """
        Updates the stock of an item in Shop

        `item_name`: name of the item to update
        
        `stock`: units to add to the item
        """
        self.items[item_name]['stock'] += units
        print('{} has been updated with {} more units'.format(item_name, units))

    def update_price(self, item_name, new_price):
        """
        Updates the price of an item in Shop

        `item_name`: name of the item to update

        `new_price`: updated price for the item
        """
        self.items[item_name]['price'] = new_price
        print('The price of {} has been updated to {}'.format(item_name, new_price))
    
    def sale(self, item_name, units):
        """
        Performs transaction on Shop items

        `item_name`: the name of the item to sale

        `units`: the number of the item to sale
        """
        self.items[item_name]['stock'] -= units
        receipt = {
            'item': item_name,
            'price': self.items[item_name]['price'],
            'units': units,
            'total': units * self.items[item_name]['price']
        }
        transaction_id = len(self.transactions)+1
        self.transactions[transaction_id] = receipt
        print("___{}___\nThank you for shopping with us\nItem: {}\nPrice:{}\nUnit:{}\nTotal:{}".format(
            self.name,
            receipt.get('item'), 
            receipt.get('price'), 
            receipt.get('units'), 
            receipt.get('total'), 
        ))

    def find_transaction(self, transaction_id):
        """
        Returns information about a transaction from Shop

        `transaction_id`: the id of the queried transaction
        """
        receipt = self.transactions[transaction_id]
        print("----Receipt----\nItem: {}\nPrice:{}\nUnit:{}\nTotal:{}".format(
            receipt.get('item'), 
            receipt.get('price'), 
            receipt.get('units'), 
            receipt.get('total'), 
        ))
    
    def report(self):
        """
        Returns information about all transaction from Shop
        """
        sold = 0
        revenue = 0

        for transaction_id in self.transactions:
            sold += self.transactions[transaction_id]['units']
            revenue += self.transactions[transaction_id]['total']
        print("Transaction Report:\nSOLD:{}\n REVENUE: {}".format(sold, revenue))
    

shop1 = Shop("Kanti Plus")

shop1.add_item('Coke', 250, 50)
shop1.add_item('Maggi', 1000, 25)
shop1.add_item('Garri', 1000, 100)
shop1.add_item('Rice', 2000, 50)

shop1.sale('Maggi', 2)
shop1.sale('Coke', 12)
shop1.sale('Garri', 10)
shop1.sale('Rice', 10)

shop1.find_transaction(2)

shop1.report()

# Q3. Create a Game class that allows users to create their own games
# your class should allow users to create from a list of at least one game.
# You can decide the game to design in your class.
# Your game must be rebost enough for users to interact with it.