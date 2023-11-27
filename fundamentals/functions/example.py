# Whats a function?
"""
A fuction is a group code that solves a specific problem.
Or does a specific task.
"""

# Built In Functions

# Print
print("I am a man")

# Type
thetype = type(1)

# Input
# name = input("What is your name? \n")

def specialPrint(value):
    print("--------------")
    print(value)
    print("--------------")

specialPrint("Nur Aliyu")
specialPrint("Some other infromation")

def printSum(num1, num2):
    print(num1+num2)

printSum(10, 20)
printSum(10, 120)

def countTo10():
    for i in range(1, 11):
        print(i)

countTo10()

def doSum(num1=0, num2=0):
    print(num1+num2)

doSum(10, 5)

def getSum(num1, num2):
    return num1+num2

number = getSum(5, 7)
print(number)
number = getSum(15, 17)
print(number)

print("\n")
print("\n")

def getPrimeWithin(start, end):
    for num in range(start, end):
        factors = 0
        for divisor in range(2, num):
            if num % divisor == 0:
                factors += 1
        if factors == 0:
            print(num)

getPrimeWithin(2, 10)
print("\n")
getPrimeWithin(10, 35)
print("\n")
getPrimeWithin(3, 6)

print("\n")
print("\n")

def playeFootBallGame(players):
    index = 0
    score = 0

    while len(players) > index:
        player = players[index]
        index += 1
        skills = "Speed: {}\nAccuracy: {}".format(player.get('speed'), player.get('accuracy'))
        guess = input("Guess the player with the following skills:\n{}\n:".format(skills))
        if len(guess.lower().strip().split()) > 1:
            if ((guess.lower().strip().split()[0] == player.get('name').lower().split()[0]) and (guess.lower().strip().split()[-1] == player.get('name').lower().split()[-1])) or ((guess.lower().strip().split()[-1] == player.get('name').lower().split()[0]) and (guess.lower().strip().split()[0] == player.get('name').lower().split()[-1])):
                print("Correct")
                score += 5
            else:
                print("Wrong")
                score -= 3
        elif len(guess.lower().strip().split()) == 1:
            if (guess.lower().strip().split()[0] in player.get('name').lower()) and (guess.lower().strip().split()[-1] in player.get('name').lower()):
                print("Correct")
                score += 5
            else:
                print("Wrong")
                score -= 3

    print("Your score is: {}".format(score))


players_set1 = [
    {
        "name": "Lionel Messi",
        "speed": 99,
        "accuracy": 99,
    },
    {
        "name": "Erling Halland",
        "speed": 89,
        "accuracy": 89,
    },
    {
        "name": "Kylian Mbappe",
        "speed": 98,
        "accuracy": 98,
    },
    {
        "name": "Cristiano Ronaldo",
        "speed": 78,
        "accuracy": 78,
    },
]

players_set2 = [
    {
        "name": "Jude Belingham",
        "speed": 95,
        "accuracy": 99,
    },
    {
        "name": "Vini. Jnr.",
        "speed": 89.9,
        "accuracy": 89,
    },
    {
        "name": "Neymar Jnr.",
        "speed": 98,
        "accuracy": 98,
    },
    {
        "name": "Karim Benzima",
        "speed": 98,
        "accuracy": 88,
    },
]

# playeFootBallGame(players_set2+players_set1)

# Exercise
# Q1. Write a function that returns the product of two numbers
#  Test the function by calling it 3 times with 3 different set of numbers