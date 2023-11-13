# Q1. Write a function that takes 3 numbers and prints the first number
# as it's, the second number multiplied by 3 and the third number raised
#  to the power of 3. e.g. yourfunction(1, 2, 3) => 1, 6, 27

def command1(num1=4,num2=2,num3=3):
    print(num1*1,num2*3,num3**3)
command1(4,2,3)
print("")
# Q2. Write a function that takes a list of 6 numbers and return
# all the even numbers in a new list 
# e.g. yourfunction([1,2,3,4,5,6]) => [2, 4, 6]
def command2(numbers):
    even_numbers = []
    for num in numbers:
      if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers
even_numbers= [11,12,13,14,15,16,17]
print(command2(even_numbers))
        
            
# Q3. Write a function that takes a string of alphabets and prints out
# all the vowels found in the string without repetition.
# e.g. yourfunction('mystring is here') => 'ie

def letters(alpha):
    vowels="aeiou"
    v=[]
    for alph in alpha:
        if alph.lower() in vowels:
            if alph.lower() not in v:
                v.append(alph.lower())
    return v
print(letters("My nAme is NUr"))            
    
    
