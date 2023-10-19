# Dictionary is a datatype that is stored within curly brackets and it
# has a key and value pairs seperated by comma.

person = {"name":"Umar Isa", "age":16, "height":2.5, "weight":65.9}

classroom = {"name":"Primary 2", "teacher":"Habib Sani", "studets":["Musa", "Omale", "Samuel"]}

print(person)
print(classroom)

# METHODS
print(person.get("name"))
print(person.get("age"))
print(person.get("xage", "x13"))

userinfo = {"name":"Nur Aliyu", "photo":"my-photo-location.jpg"}
print(userinfo.get('name'))
print(userinfo.get('photo', 'default-image.png'))

print("Before clearing")
print(person)
person.clear()
print("After clearing")
print(person)

userinfo2 = userinfo.copy()
userinfo3 = userinfo

print(userinfo2)
print(userinfo3)

print(classroom.items())
print(classroom.keys())

x = classroom.pop("name")
print(classroom)
print(x)
y = classroom.popitem()
print(classroom)
print(y)

classroom.setdefault("name", x)
classroom.setdefault(y[0], y[1])
print(classroom)

classroom.update(userinfo)
classroom.update({"teacher":"Shedrack Yusuf", "students":["Amin Mohd", "Saminu Idris"]})
classroom.update([("name", "Aisha Aliyu"), ("age", "16")])
print(classroom)

print(classroom.values())

# OPERATIONS
print(classroom["name"])
print(classroom["age"])
classroom["age"] = 35
print(classroom["age"])
classroom["test"] = 25
classroom.setdefault("age", 19)
classroom["age"] = 19
classroom.update({'age':20})
print(classroom)