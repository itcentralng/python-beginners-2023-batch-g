# Strings are datatypes within qoutations - double or single

name = "Hassan"
age = "19"
address = "Kakuri Road, Kawo Kaduna"

# Methods
name = "aliyu"
print(name.capitalize())

person = "MAsud"

print(person.casefold())

place = "Kaduna"

print(place.center(12, "*"))

print(place.count('a', 0, 6))

# Exercise:
# example :
text = "hassan"
print(text.capitalize())

country = "EGYPT"
print(country.casefold())

text = "apple"
print(text.center(12, "y"))

name2 = "khadija"
print(name2.count("h"))

player = "cristiano"
print(player.count("i"))

phone = "+234701231212"
phone2 = "+233701231212"
nigerian_ext = "+234"
print(phone.startswith(nigerian_ext))
print(phone2.startswith(nigerian_ext))

# STRING OPERATIONS
print(player[0])
print(player[0:6])
print(player[0:6:3])
print(player[::3])
print(player[::-1])