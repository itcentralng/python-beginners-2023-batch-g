# Q1. Create a variable to hold the string "AHMAD" and change all occurances of
# "A" with "O"

name = "AHMAD"
name = name.replace("A", "O")
print(name)

# Q2. Create an empty list and append all items in the above variable using the
# appropraite list method
chars = []
chars.extend(name)
print(chars)

# Q3. Using list slicing, get the first two characters from the list above
print(chars[:2])
# Q4. Without using the reverse method, reverse the list above
chars = chars[::-1]
print(chars)
# Q5. Using the reversed list, create a new string and store it in a new variable
new_string = "".join(chars)
print(new_string)
# Q6. Create an empty list and append individual characters from the new string
new_list = []
new_list.extend(new_string)
print(new_list)
# Q7. Remove the last character from the list and store it in a new variable
new_variable = new_list.pop()
print(new_variable)