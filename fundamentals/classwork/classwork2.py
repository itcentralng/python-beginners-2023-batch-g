# Q1. Create a tuple holding 3 items
t = "Father", "Mother", "Son"
print(t)
# Q2. Using the tuple above, create a new string
s = "".join(t)
print(s)
# Q3. Create an empty list and append individual items from the tuple
l = []
l.extend(t)
print(l)
# Q4. Append the uppercase version of the new string to the new list
l.append(s.upper())
print(l)
# Q5. Create a new list and append lower case characters from the last item of the new list
l2 = []
l2.extend(l[-1].lower())
print(l2)
# Q6. Count the number of occurences of the first item in our main tuple
print(t.count(t[0]))
# Q7. Get the index of the new string from the new list
print(l.index(l[-1]))