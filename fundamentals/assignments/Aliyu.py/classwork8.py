#1. Write a football game where user is prompted with a player
# skills rating and is asked to guess the player.If they guess the right
# they get 5 pionts,if they guess the wrong they 3 pionts get deducted
# at the end of the game,user is shown their performance.


#EA24=True
#index=0
#score=0

#players=[{"player":"MESSI","SPEED":88,"SHOOTING":90},
            #{"player":"MBAPPE","SPEED":95,"SHOOTING":91},
            #{"player":"HALLAND","SPEED":94,"SHOOTING":95},
            #{"player":"GAVI","SPEED":83,"SHOOTING":87},
            #{"player":"NUR","SPEED":80,"SHOOTING":79}
    #]

#while len(players) >(index) :
    #SPEED=players.get('SPEED')
    #SHOOTING=players.get('SHOOTING')
    #answer=input("GUESS THE PLAYER WITH THE SPEED OF {} AND SHOOTING OF {}:".format(SPEED, SHOOTING))

    #if answer.lower() in players:
        #print("correct answer. you earn 5 points")
    
    #score +=5
    #print('your score')

#else:
 #   print("wrong answer,you losr 3 points")
  #  score -=3

#index += 1
#print('your final score {} :'.format(score))


#EA24=False


#correction
players = [  {
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
