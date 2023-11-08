# # Q1. Using while loop, loop through numbers 1 - 10 and
# # print out the result of multiplying each number by 3.

# # for i in range(1, 11):
# #     print(i*3)

# # for i in range(1, 6):
# #     print(i)

# # Q2. Write a code to find all prime numbers between 2 and 35 inclusive.

# for number in range(2, (35+1)):
#     isPrime = True

#     for i in range(2, number):
#         if number % i == 0:
#             isPrime = False
    
#     if isPrime == True:
#         print(number)

# for num in range(2, 35+1):
#     for prime in range(2, num):
#         if num % prime == 0:
#             break
#     else:
#         print(num)

for num in range(2, 8):
    print("CURRENT NUMBER: ", num)
    factors = 0
    print("STARTING FACTORS: ", factors)
    for divisor in range(2, num):
        print(num, divisor)
        if num % divisor == 0:
            print("Yup it can divide perfectly")
            factors += 1
        else:
            print("Nope it cant divide perfectly")
    print("FINAL FACTORS: ", factors)
    if factors == 0:
        print("PRIME: ", num)