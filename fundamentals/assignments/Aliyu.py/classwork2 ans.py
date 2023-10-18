#1
tuple="father","mother","son"
print(tuple)

#2
newstring=""
x="".join(tuple)
print(x)

#3
list=[]
list.extend(tuple)
print(list)

#4
list.append(x.upper())
print(list)

#5
list2=[]
list2.extend(list[3].lower())
print(list2)

#6
print(tuple.count(list[0]))

#7
print(list.index(list[-1]))