#Q1
def getconsonant(alphabets: str):
    consonants = ["bcdfghjklmnpqrstvwxyz"]
    nonrepetingconsonants = []
    for alphabet in alphabets.lower():
        if alphabet in consonants:
            if alphabet not in nonrepetingconsonants:
                nonrepetingconsonants.append(alphabet)
    print(",".join(nonrepetingconsonants))

def getconsonants(alphabets: str):
    print(",".join(set([alphabet for alphabet in alphabets.lower() if alphabet in "bcdfghjklmnpqrstvwxyz"])))

getconsonants("assignments")

#Q2
def integers(numbers):
    nums = []
    for number in numbers:
        if number %2 ==0:
            nums.append(number)
        else:
            nums.append(number*2)
    return nums

x =integers([1, 2, 3, 4])
print(x)

#Q3
def listofitems(arranged):
    arranged.sort(key=lambda dic: dic["name"], reverse=False)
    return arranged

x = listofitems([{"name":"bashir"},{"name":"ahmad"}])
print(x)