#1.extend:it used to add elements of an iterable to an existing list
cars=["ferrari","bugatti","benz"]
cars2=["toyota","bmw"]
cars.extend(cars2)
print(cars)

#2.pop:it removes an element from a list temporary
fruits=["apple","pear","orange"]
print(fruits.pop(1))
print(fruits)

#3.remove:it removes a character from a list permanently
names=['musa','abdul','josh']
names.remove('abdul')
print(names)

#4.index:returns the first element with the specified index value
places=["lagos","zaria","kano"]
print(places.index("kano"))

#5.insert:adds an element at the specifed value at the specifed locaion
laptops=["dell","lenovo","asus"]
laptops.insert(1,"hp")
print(laptops)

#6.reverse:reveres the order of the list
description=["hot","cold","warm","freezning"]
description.reverse()
print(description)

#7.sort:it sorts th list in either ascending or desedng but it sorts in ascending by defult
cars3=["ford","bentley","gbox","porche"]
cars3.sort(reverse=True)
print(cars3)

cars3.sort()
print(cars3)