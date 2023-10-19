#1
v="A2Z"
print(v)

#2
w=v[1:2]
print(w)

#3
tuple=(v,w)
print(tuple)

#4
list=[v,w]
print(list)

#5
j=False
i=True
list.extend((i,j))
print(list)

#6
integer=2023
print(integer)

#7
weight=99.7
print(weight)

#8
list.extend((integer,weight))
print(list)

#9
list2=[]
list2.extend(list[2:6])
print(list2)

#10
list2.reverse()
print(list2)

print(list2[::-1])