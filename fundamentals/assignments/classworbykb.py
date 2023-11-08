# Q1. Write a function that takes 3 numbers and prints the first number
# as it's, the second number multiplied by 3 and the third number raised
#  to the power of 3. e.g. yourfunction(1, 2, 3) => 1, 6, 27
def sums(num1,num2,num3):
    print(num1*num2*num3)
sums(10, 2 ,4)
sums(10, 12,4)
sums(20,10,3)

# Q2. Write a function that takes a list of 6 numbers and return
# all the even numbers in a new list 
# e.g. yourfunction([1,2,3,4,5,6]) => [2, 4, 6]
def geteven(evens):
    for num in range(2,evens):
        if num %2==0:
            print(num)
geteven(7)

    


# Q3. Write a function that takes a string of alphabets and prints out
# all the vowels found in the string without repetition.
# e.g. yourfunction('mystring is here') => 'ie'
