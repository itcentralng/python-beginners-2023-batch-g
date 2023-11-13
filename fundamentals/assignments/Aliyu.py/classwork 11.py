
#Q4. Write a function that takes a list of dictionaries and returns
# an ordered list of dictionaries where the dictionary with the highest score
# comes first while the one with the lowest score comes last.
# e.g. mylist = [{'score':20, 'name':'Ibrahim'}, {'score':40, 'name':'Sani'}]
#yourfunction(mylist) => [{'score':40, 'name':'Sani'}, {'score':20, 'name':'Ibraim'}]


def findScore(dic):
    return dic['score']
def listSorter(scores: list):
    scores.sort(key=findScore, reverse=True)
    return scores

x = listSorter([{'score':20, 'name':'Ibrahim'}, {'score':10, 'name':'Sani'}, {'score':30, 'name':'Zainab'}])
print(x)

    

#Q1. Create a function that will take a string of alphabets and returns a list 
#of non repeating consonant using list comprehension.
#e.g. yourfunc("musa") => ["m", "s"]
#Bonus point if you can return it this way => "ms"

def getconst(letters: str) :
    not_const="aeiou"
    print("".join(alph for alph in letters.lower() if alph not in not_const ))

getconst("omale abu")    



#Q2. Write a function that takes a list of numbers and return a even numbers as they are
# and all odd numbers doubled. e.g. yourfunc([1, 2, 3, 4]) => [2, 2, 6, 4]

def unique_num (numbers) :
    digits=[]
    for num in numbers:
        if num %2==0 :
            digits.append(num)
        else:
                digits.append(num*2)
    return digits
digits=[1,2,3,4,5,6,7,8,9,10]
print(unique_num(digits))



#Q3.Write a function that takes a long integer and returns an intergger
#with each number doubled. e.g. yourfun(234) => 468

def yourfun(numb: int) :
    # convt the int to an iterable string
    nu= str(numb)
    #create a variable to store the updated number
    storage=[]
    #loop through the string
    for d in nu:
          #convert the current number in loop to an int and double it
          d_digit=int(d)*2
          #add the str verion of the numbr to the storage var
          storage.append(str(d_digit))
    #return the final storage variable
    return "".join(storage)     

x=123456789
print(yourfun(x))             



#Q4. Write a fuction that takes a list of dictionaries and 
#return a list sorted alphabetically by name 
#e.g. yourfun([{'name':'Bashir'}, {'name':'Ahmad'}]) => [{'name':'Ahmad'}, {'name':'Bashir'}]

def sorter(names) :
     names.sort(key=lambda b: b['name'],reverse=False)
     return names
l=sorter([{'name':'nur'},{'name':'omale'},{'name':'mr teey'}])
print(l)





        


