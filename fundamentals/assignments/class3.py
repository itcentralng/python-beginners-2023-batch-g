from class1 import Game

testgame = Game('Hulla Hulla')

testgame.add_questions([
    {'question':'How old am I?', 'answer':'12'},
    {'question':'How much sugar do I take a day?', 'answer':'50 spoons'},
])

testgame.play()