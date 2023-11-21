invited_guests = ['Zainab', 'Nur', 'Omale']
secret_code = "house"

guest1 = input("Whats the secret code? : ")
if guest1 == secret_code:
    name = input("Tell us your name: ")
    if name in invited_guests:
        print("Welcome to the party ", name)
    else:
        print('Secret thief!!!')
else:
    print("Get out bro!")
guest2 = input("Whats the secret code: ")
if guest2 == secret_code:
    name = input("Tell us your name: ")
    if name in invited_guests:
        print("Welcome to the party ", name)
    else:
        print('Secret thief!!!')
else:
    print("Get out bro!")

guest3_secret = input("Whats the secret code: ")
guest3_name = input("Tell us your name: ")

if (guest3_secret == secret_code) or (guest3_name in invited_guests):
    print("welcome to the party", guest3_name)
else:
    print("Get out!!")


purchased_ticket_type = "Road"

if purchased_ticket_type == 'Air':
    print("We travel")
elif purchased_ticket_type == 'Train':
    print('We still travel')
else:
    print("No travelling")