# Q1. Write a function that takes 3 numbers and prints the first number
# as it's, the second number multiplied by 3 and the third number raised
#  to the power of 3. e.g. yourfunction(1, 2, 3) => 1, 6, 27

def doubler(num1, num2, num3):
    num2 *= 3
    num3 **= 3
    print("{}, {}, {}".format(num1, num2, num3))

doubler(2, 4, 6)
doubler(1, 2, 3)

# Q2. Write a function that takes a list of 6 numbers and return
# all the even numbers in a new list 
# e.g. yourfunction([1,2,3,4,5,6]) => [2, 4, 6]

def getEvenNUmbers1(numbers):
    evens = []
    for number in numbers:
        if number % 2 == 0:
            evens.append(number)
    return evens

def getEvenNUmbers2(numbers):
    return [number for number in numbers if number % 2 == 0]

x = getEvenNUmbers1([1,2,3,4,5,6])
print(x)
x = getEvenNUmbers2([10,12,13,14,15,16])
print(x)

# Q3. Write a function that takes a string of alphabets and prints out
# all the vowels found in the string without repetition.
# e.g. yourfunction('mystring is here') => 'ie'

def getVowels(alphabets: str):
    vowels = "aeiou"
    nonrepeatingvowels = []
    for alphabet in alphabets.lower():
        if alphabet in vowels:
            if alphabet not in nonrepeatingvowels:
                nonrepeatingvowels.append(alphabet)
    print(''.join(nonrepeatingvowels))

def getVowels(alphabets: str):
    print("".join(set([alphabet for alphabet in alphabets.lower() if alphabet in "aeiou"])))

getVowels("Emmae")

#Q4. Write a function that takes a list of dictionaries and returns
# an ordered list of dictionaries where the dictionary with the highest score
# comes first while the one with the lowest score comes last.
# e.g. mylist = [{'score':20, 'name':'Ibrahim'}, {'score':40, 'name':'Sani'}]
# yourfunction(mylist) => [{'score':40, 'name':'Sani'}, {'score':20, 'name':'Ibraim'}]


def listSorter(scores):
    scores.sort(key=lambda dic: dic['score'], reverse=True)
    return scores

x = listSorter([{'score':20, 'name':'Ibrahim'}, {'score':10, 'name':'Sani'}, {'score':30, 'name':'Zainab'}])
print(x)

def findScore(dic):
    return dic['score']

def listSorter(scores: list):
    scores.sort(key=findScore, reverse=True)
    return scores

x = listSorter([{'score':20, 'name':'Ibrahim'}, {'score':10, 'name':'Sani'}, {'score':30, 'name':'Zainab'}])
print(x)

def findHighest(mylist):
    highest = 0
    highestItem = {}
    for item in mylist:
        if item.get('score') > highest:
            highest = item.get('score')
    for item in mylist:
        if item.get('score') == highest:
            highestItem = item
    return highestItem

def listSorter(scores: list):
    sortedItems = []
    items = len(scores)
    for i in range(items):
        highest = findHighest(scores)
        sortedItems.append(highest)
        scores.remove(highest)
    print(sortedItems)

listSorter([{'score':20, 'name':'Ibrahim'}, {'score':10, 'name':'Sani'}, {'score':30, 'name':'Zainab'}])

# Q1. Create a function that will take a string of alphabets and returns a list 
# of non repeating consonant using list comprehension.
# e.g. yourfunc("musa") => ["m", "s"]
# Bonus point if you can return it this way => "ms"

# Q2. Write a function that takes a list of numbers and return a even numbers as they are
# and all odd numbers doubled. e.g. yourfunc([1, 2, 3, 4]) => [2, 2, 6, 4]

# Q3. Write a function that takes a long integer and returns an intergger
#  with each number doubled. e.g. yourfun(234) => 468

# Q4. Write a fuction that takes a list of dictionaries and 
# return a list sorted alphabetically by name 
# e.g. yourfun([{'name':'Bashir'}, {'name':'Ahmad'}]) => [{'name':'Ahmad'}, {'name':'Bashir'}]