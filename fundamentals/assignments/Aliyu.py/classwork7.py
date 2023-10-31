#loop through a list of numbers from 1-20 and print out the
#even numbers and any number that is divisible by 5.

numbers=[1,2,3,4,5,6,7,8,9,10]

print("EVEN NUMBERS")
for next in numbers :
    if next%2 ==0 :
        print(next)

print("DIVISIBLE BY 5")
for next in numbers:
    if next%5 ==0 :
        print(next)        