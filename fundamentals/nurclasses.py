
# Q3. Create a Game class that allows users to create their own games
# your class should allow users to create from a list of at least one game.
# You can decide the game to design in your class.

class Game:
    def __init__(self, name):
        """
        Create games by choosing `name`.
        """
        self.name = name
        self.questions = []
        self.player=[]


    def add_questions(self, questions):
        self.questions.extend(questions)
        print("{} questions added to {} successfully!".format(len(questions), self.name))

    
    def play(self,player):
        player=input("Type your name for the games : ")
        self.player.append({'name':player,'score':0})
        
        print("{}\n\n {} are you ready?\nLets begin:\n".format(self.name,self.player))
        playing = True
        while playing:
            question = (self.questions)
            print(question.find('question'))
            if question.get('options'):
                for option in question.get('options'):
                    print('- '+option)
            response = input('\n: ')
            if response.strip().lower() == 'q' or response.strip().lower() == 'quit' or response.strip().lower() == 'exit':
                playing = False
            elif response.strip().lower() == question.get('answer').strip().lower():
                print('Thats correct you earn 5 pionts!')
                self.player[-1]['score'] +=5
            else:
                print('Opps thats wrong you lose 3 pionts, the right answer is {}'.format(question.get('answer')))
                self.player[-1]['score'] -=3
        
                

firstGame = Game('Guess or Die')
secondGame = Game('Quiz of Life')
thirdGame = Game('Foodball is Life')

questions1 =  [{
                'question':"How old was Nur when he got his first tooth?",
                'options':[
                    '10 years',
                    '1 year',
                    '2 years',
                ],
                'answer': '1 year'
            },
            {
                'question':"What is Alameen's favorite thing?",
                'options':[
                    'Reading',
                    'Swimming',
                    'Food',
                ],
                'answer': 'Food'
            },
            ]

questions3 =  [{
                'question':"Who scored the winning goal in the 2014 world cup finals?",
                'options':[
                    'Gotze',
                    'Messi',
                    'Muller',
                ],
                'answer': 'Gotze'
            },
            {
                'question':"Who sponsors Real Madrid?",
                'options':[
                    'Spotify',
                    'Sporty',
                    'Emirates',
                ],
                'answer': 'Emirates'
            },
            ]

questions2 =  [{
                'question':"I am slim and burny what am I?",
                'answer': 'match stick'
            },
            {
                'question':"I let you travel through time without actually doing so, what am I?",
                'answer': 'book'
            },
            ]

firstGame.add_questions(questions2)
secondGame.add_questions(questions1)
thirdGame.add_questions(questions3)
thirdGame.add_questions(questions1)
thirdGame.add_questions(questions2)
thirdGame.play('nur')

# Q4. Upgrade the game class to manage players:
# there names, their scores and a leaderboard