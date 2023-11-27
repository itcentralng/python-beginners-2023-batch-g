# Loop through a list of numbers from 1 - 20 and print out the
# even numbers and any number that is divisble by 5.

numbers = [10, 20, 30, 40, 50, 55, 53]

for next in numbers:
    if next%2 == 0 or next%5 == 0:
        print(next)