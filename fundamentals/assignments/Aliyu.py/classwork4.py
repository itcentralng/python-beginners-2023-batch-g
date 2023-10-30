# Q1. Create 4 variables and add them all together and print the result
# Q2. Create a variable with the value 6 and update it to 10 with the appropraite operator
# Q3. Compare all variables in Q1 above
# Q4. Create a shopping list and check if you have 'mango' in there
# Q5. Chain all comparison in Q3 above with all our logical operators


#1
v1=[8]
v2=[20]
v3=[6]
v4=[5]
print(v1+v2+v3+v4)

#2
num=6
num+=4
print(num)

#3
print(v1==v2==v3==v4)

#4
list=["pears","mango","apple","burger"]
print("mango" in list)

#5
print(v1 or v2)
print(v3 and v4)
print(not v3 or v4)