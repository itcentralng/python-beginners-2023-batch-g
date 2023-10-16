# A list is a container like data that stores other datatypes within
# a square bracket, each data is seperated from the other using comma

people = ["Ahmad", "Ibrahim", "Umar"]

items = ["James", True, 23, 5.5, [1, 2, 3]]

print(people)
print(items)

# METHODS

people.append("Aliyu")
people.append("Musa")
people.append("Samuel")
print(people)

people.clear()
print(people)

people.append("Samuel")
people.append("Samuel")
people.append("Samari")
print(people)
print("BEFORE COPY")

people2 = people.copy()
print(people)
print(people2)

people.clear()

print(people)
print(people2)

print(people2.count('Ahmad'))
print(people2.count('Samuel'))

# LIST OPERATIONS
print(people2[0])
print(people2[1])
print(people2[2])
print(people2[1:3])
print(people2[::-1])