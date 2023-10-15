#find:it is used to find a specific substring in a string
text="he is a tall boy"
print(text.find("is"))

#format:formats a specific value in a string
numbers="7"
argument="messi has {} balln d`or".format(numbers)
print(argument)

#index:it is used to access individual values within a string
text="she has a baby"
print(text[3:7])

#isalnum:is a method that shows whether all characters in a string are alphanumeric using true or false
text="adamu is 2 years old"
print(text.isalnum())
text2="hello69"
print(text2.isalnum())

#isalpha:is a method that shows wether all characters in a string are only alpbabetic using true or false
country="nigeria"
print(country.isalpha())

#isdecimal:it used to show whether all character in a string are decimal digits or not
text="1457755577"
print(text.isdecimal())

#islower:it is used to check whether all the charcters in a string are all in lower case
boxer="muhammad ali"
print(boxer.islower())

#isupper:it is used to check whether all the chracters in a string are in upper case
name="ALIyu"
print(name.isupper())

#upper:converts all the lower case alphabets in a string to upper cases
place="nairobi34"
print(place.upper())

#lower:converts all the upper case alphabets in a string to lower cases alphabets
convert="UPPERCASE"
print(convert.lower())

#replace:this method replaces the occurrences of a character with a new character within the same string
prefrence="i like dogs,dogs are peacful"
print(prefrence.replace("dogs","cats"))

#split:it splits a string into a list of substrings
fruits="apple,banana,orange,pear"
print(fruits.split(","))

#strip:removes unimportant chracters in a string
nonsense="$$$dollars$$$"
print(nonsense.strip("$"))

#join:it is used to merge elements of either a list or tuple into a single string
merge=["join","us","please"]
print("-".join(merge))

#istitle:it checks if each word in a string starts with an uppercase
conclusion="I Am Tired"
print(conclusion.istitle())


