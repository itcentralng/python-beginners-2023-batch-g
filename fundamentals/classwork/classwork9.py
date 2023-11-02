# Q1. Answer Question 1 again from the previous class and upgrade it
#  such that the user is allowed to enter players fullname, first
#  or last name

players = [
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