<<<<<<< HEAD
number=0

while number <10:
    number +=1
    print(number)
=======
number = 0

while number < 10:
    number + 1
    number += 1
    number = number + 1
    number += 1
    number + 1
    print(number)


playing = True
index = 0

while playing:
    states = [
        {"name":"Niger", "capital":"Minna"},
        {"name":"Lagos", "capital":"Ikeja"},
        {"name":"Anambra", "capital":"Awka"},
    ]

    capital = states[index].get('capital')
    state = states[index].get('name')
    answer = input("What is the capital of {}: ".format(state))

    if capital.lower() == answer.lower().strip():
        print("Thats correct")
    else:
        print("Incorrect, the capital of {} is {}".format(state, capital))
    
    index += 1
    
    if index >= len(states):
        playing = False
>>>>>>> 43f26411cf84295d9d48ec419004e9135f894b5a
