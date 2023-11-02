# Q1. Write a football game where a user is prompted with a player
#     skills rating and is asked to guess the player. If they guess right
#     they get 5 points, if they guess wrong 3 points get deducted.
#     At the end of the game, user is shown their performance.

# Pseudocode:
"""
- Create a list of players
- Let's start a loop with the starting index 
  being compared to the len of players
- Select a player from the list of players
    - have a starting index - before the loop
    - increase the starting index by 1 each time
- Show that players skills to the user
- Ask the user to guess the player
- If the guess is correct we award 5 points to the user
    - have a starting score - before the loop
- if wrong we deduct 3 points from the users points
- We continue till we exhaust the list of players
- Show the user their score
"""

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
    if guess.lower().strip() in player.get('name').lower():
        score += 5
    else:
        score -= 3

print("Your score is: {}".format(score))

# Q2. Write a tailoring game where a user is asked to enter their
#     dress information including length, width and neck size based
#     on the users input, you show the user a list of fitting dresses
#     from your dress collection.

# # Pseudocode:
# """
# - Create a list of dresses in a dictionary
# - allow the user to input their length
# - allow the user to input their width
# - allow the user to input their neck size
# - create a variable to store fitting dresses
# - Loop through our list of dictionaries
# - Check for a size that fits the user
# - If we find the one that fits:
#     - add it to the fitting dresses
# - at the end of the loop:
#     - Check our list of fitting dresses
#     - if at least a dress is found, we show the user the dresses
#     - else, we tell the user sorry
# """

# dresses = [
#     {
#         "name": "Dress 1",
#         "brand": "Nike",
#         "neck-size": 3,
#         "width": 15,
#         "length": 30
#     },
#     {
#         "name": "Dress 2",
#         "brand": "Balenciaga",
#         "neck-size": 13,
#         "width": 35,
#         "length": 60
#     },
#     {
#         "name": "Dress 3",
#         "brand": "Dior",
#         "neck-size": 12,
#         "width": 34,
#         "length": 59
#     },
# ]

# length = input("Input the length of your dress: ")
# length = int(length)
# width = input("Please enter your choice of width: ")
# width = int(width)
# neck_size = input("Please enter your neck size: ")
# neck_size = int(neck_size)

# fitting_dresses = []

# for dress in dresses:
#     if (length == dress.get('length')) or (length == dress.get('length')+1) or (length == dress.get('length')-1):
#         if (width == dress.get('width')) or (width == dress.get('width')+1) or (width == dress.get('width')-1):
#             if (neck_size == dress.get('neck-size')) or (neck_size == dress.get('neck-size')+1) or (neck_size == dress.get('neck-size')-1):
#                 fitting_dresses.append(dress)

# if len(fitting_dresses) > 0:
#     if len(fitting_dresses) == 1:
#         response = "Here's a dress that can fit:\n\n"
#     else:
#         response = "Here are dresses that can fit:\n\n"

#     for dress in fitting_dresses:
#         response+="name: {}\nbrand: {}\nlength: {}\nwidth: {}\nneck-size: {}\n\n".format(dress.get('name'), dress.get('brand'), dress.get('length'), dress.get('width'), dress.get('neck-size'))
#     print(response)
# else:
#     print("Sorry, no fitting dress found")
    