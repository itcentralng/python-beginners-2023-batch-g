students = ["Omale", "Mohd", "Nur", "Alameen"]
alphabets = "ABCDEFGHIJKLMONPQRSTUVWXYZ"

people = []

for next in students:
    person = {
        "name":next,
        "characters":len(next),
        "firstChar": next[0],
        "lastChar": next[-1],
        "reversed": next[::-1],
        "containsA": 'a' in next,
        "lastIndex": len(next)-1
    }
    people.append(person)

print(people)

name = "Shedrack"
for char in name:
    print(char.upper())

person = {
    "name":"Aisha Ibrahim",
    "age": 16,
    "hobbies": [ "swimming", "running" ]
}

for a in person:
    if a == 'hobbies':
        for x in person.get('hobbies'):
            if 'i' in x.lower():
                print(x)
    else:
        print(person.get(a))


players = [
    {
        "name":"Lionel Messi",
        "age": 35,
        "performance":99
    },
    {
        "name":"Jude Belignham",
        "age": 20,
        "performance":89
    },
    {
        "name":"Cristiano Ronaldo",
        "age": 38,
        "performance":89
    },
    {
        "name":"Kylian Mbape",
        "age": 24,
        "performance":91
    },
]

ballondior = []

for player in players:
    if player.get('performance') > 95:
        ballondior.append(player.get('name'))

print(ballondior)

retirement = []
for player in players:
    if player.get('age') > 30:
        retirement.append(player.get('name'))

print(retirement)