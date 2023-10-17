# For each of the following list methods,
# explain how it works with an example

# 1. extend
items = [1, 2, 3, 2]
# items.extend("aliyu".upper())
# items.extend(["A", "B", "C"])
items.extend(["Test", 50, 50, 1.5, True, False, [1, 2], (3, 4), {"name":"Omale"}])
print(items)
# 2. pop
x = items.pop(0)
y = items.pop()
a = items.pop()
b = items.pop()
c = items.pop()
d = items.pop()
z = items.pop()
print(y)
print(c)
print(items)
# 3. remove
items.remove(50)
print(items)
# 4. index
print(items.index(2))
print(items.index(2, 1))
# 5. insert
items.insert(0, 1)
items.insert(5, 50)
print(items)
# 6. reverse
items.reverse()
print(items)
# 7. sort
items.pop(2)
items.sort(reverse=True)
print(items)

items2 = ["Umar", "Ahmad", "Sani", "Bala"]
items2.sort(reverse=True)
print(items2)
