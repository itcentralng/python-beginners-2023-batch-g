# Q1. Create a invoice generator that asks users to enter the names of 3 items 
# they want to purchase each with its unit from a shop and it generates 
# and invoice for them.

# Pseudocode:
# - Create a list that stores all the items available in the shop with
#   their units and price tag
# - Show the user the available items
# - Allow the user to choose the items one by one with their quantity
# - Calculate all items selected and present the invoice to the user

database = {
    "mango":{'price':400, 'unit':3},
    "coffee":{'price':1500, 'unit':5},
    "coke":{'price':250, 'unit':10},
    "biscuit":{'price':100, 'unit':15},
    "milk":{'price':200, 'unit':7},
}

print(f"------------ITEMS IN KABIR'S SHOP------------")
print("-----ITEM------PRICE------UNIT")
print("{} ----- {} ----- {}".format('mango', database['mango'].get('price'), database['mango'].get('unit')))
print("{} ----- {} ----- {}".format('coffee', database['coffee'].get('price'), database['coffee'].get('unit')))
print("{} ----- {} ----- {}".format('coke', database['coke'].get('price'), database['coke'].get('unit')))
print("{} ----- {} ----- {}".format('biscuit', database['biscuit'].get('price'), database['biscuit'].get('unit')))
print("{} ----- {} ----- {}".format('milk', database['milk'].get('price'), database['milk'].get('unit')))
print(f"------------ITEMS IN KABIR'S SHOP------------")

item1 = input("Choose first item please: ")
item1unit = input("How many {} do you want: ".format(item1))

item2 = input("Choose second item please: ")
item2unit = input("How many {} do you want: ".format(item2))

item3 = input("Choose last item please: ")
item3unit = input("How many {} do you want: ".format(item3))

database[item1]['unit'] = database[item1]['unit'] - int(item1unit)
database[item2]['unit'] = database[item2]['unit'] - int(item2unit)
database[item3]['unit'] = database[item3]['unit'] - int(item3unit)

print(f"------------UPDATE SHOP ITEMS------------")
print("-----ITEM------PRICE------UNIT")
print("{} ----- {} ----- {}".format('mango', database['mango'].get('price'), database['mango'].get('unit')))
print("{} ----- {} ----- {}".format('coffee', database['coffee'].get('price'), database['coffee'].get('unit')))
print("{} ----- {} ----- {}".format('coke', database['coke'].get('price'), database['coke'].get('unit')))
print("{} ----- {} ----- {}".format('biscuit', database['biscuit'].get('price'), database['biscuit'].get('unit')))
print("{} ----- {} ----- {}".format('milk', database['milk'].get('price'), database['milk'].get('unit')))
print(f"------------UPDATE SHOP ITEMS------------")

invoice = "-----------INVOICE------------\n"
invoice += "{}     ---    {}   ----    {}\n".format(item1, item1unit, database.get(item1).get('price')*int(item1unit))
invoice += "{}     ---    {}   ----    {}\n".format(item2, item2unit, database.get(item2).get('price')*int(item2unit))
invoice += "{}     ---    {}   ----    {}\n".format(item3, item3unit, database.get(item3).get('price')*int(item3unit))
invoice += "TOTAL   ---------------    {}\n".format((database.get(item1).get('price')*int(item1unit))+(database.get(item2).get('price')*int(item2unit))+(database.get(item3).get('price')*int(item3unit)))

print(invoice)