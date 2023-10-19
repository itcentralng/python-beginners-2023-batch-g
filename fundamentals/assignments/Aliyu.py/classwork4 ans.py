# Q1. Create an empty dictionary
d={}
print(d)

# Q2. Use a method to add a new value for the key "name"
d.setdefault("name","umar")
print(d)
# Q3. Create a new variable and store a tuple of the current key value pair from our dictionary
# such that the dictionary now becomes empty.
x=("name","umar")
d.popitem()
print(d)

# Q4. Use the appropraite method to update the dictionary back to its original form using our
#new variable holding its original value
d.update({"name":"umar"})
print(d)
# Q5. Use the right method to get and print out the "name" from the restored dictionary
print(d.get("name"))
# Q6. Using operation similar to list, add values for each of the following keys into th dictionary:
# - "age". "height". "weight", "hobbies"
d["age"]=17
d["height"]=34
d["weight"]=60.5
d["hobbies"]="sleeping","watching football","playing football"
print(d)

# Q7. Create a mew variable to store the value returned from removing hobbies
print(d.popitem())
# Q8. Use the appropraite method to remove all items from the dictionary
d.clear()
print(d)
# Q9. Repeat Q2-Q6 here
d.update({"name":"umar"})
print(d)
x=("name","umar")
d.clear()
print(d)
d.setdefault("name",x[1])
print(d)
print(d.get("name"))
d["age"]=17
d["height"]=34
d["weight"]=60.5
d["hobbies"]="sleeping","watching football","playing football"
print(d)



