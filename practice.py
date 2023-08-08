"""size=5
count=size*(-1);

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alpha.reverse()
for i in range(1,size+1):
        for j in range((size+size-1)-(i+i-1)):
                print("-",end="")
        for k in range(1):
                for letter in alpha[count:count-i:-1]:
                        print(letter,end="-")
        print()
for i in range(size):
        for j in range(i*2):
                print("-",end="")
        for k in range(1) :
                for letter in alpha[count-i:(size-i)*(-1):-1]:
                        print(letter,end="-")
        print()
"""
"""Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Case Changing Methods on String
>>> #lower() ==> Converts a string to lowercase
>>>  #upper() ==>converts a string to uppercase
>>> #swapcase() ==> lowercase become uppercase and vice versa
>>>  #title() ==> Converts the first character of each word to uppercase
>>> #capitalize() ==> Converts the first character to uppercase
>>> #Case Checking Methods on String
>>> #isupper() ==>Returns True if all character in the string are uppercase
>>>  #islower() ==>Returns True if all character in the string is lowercase
>>> #isalnum() ==>Returns True if all character in the string is alpha numeric


#python Build in functions for insert and delete the items from List
#append() ==> Adds an element at the end of the list
#index() ==> Returns the index of the element with the specified value
#insert() ==> Adds an element at the specified position
#remove() ==> Removes the otem with the specified value
#pop() ==>Removes the element with the specified value
#del variablename[index] ==> Removes item with the specified index
vehi=["Car","Bus","Auto","Lorry"]

#python build-in functions for list

#len() ==> Returns the length of the list
syntax :- len(list)
#reverse() ==> Reverse the order of the list
syntax :- list.reverse()
#sort() ==> Sort the list
syntax :- list.sort()
#max(),min() ==> Returns the maximum and minimum values from the list
syntax :- max(list) ,min(list)
#clear() ==> Removes all elements from the list
syntax :- list.clear()
#count() ==>Returns the no.on values with the specified value
syntax :- list.count(value)
#extend() ==> Add the elements of a list (or any iterable),
         #to the end of the current list
syntax :- list.extend(iterable)
#copy() ==> Returns the copy of the list
syntax :- list.copy()

Access Dictionary Items
1.keys() ==>It returns  a list of all the keys in the dictionary
     Syntax :-  dict.keys()
2.values() ==> It returns a list of all the values
    Syntax :- dict.values()
3.items() ==> It returns each item in a dictionary as tuple in a list
    Syntax :- dict.items()
4.get() ==> It returns the value with the specified key name
d={"name":"Dineshwaran","age":29,"mobile":1234567890,"place":"Ramnad"}

Methods for insert and delete elements

1.d[key]=value

2.update() ==> It will update the dictionary with  items from the given argument
                                  If the item does not exist, the item will be add
           # Syntax :-  d.update({key,value})
3.pop()     ==> It removes the item with specified key
            #Syntax :-  d.pop(key)
 4.popitem() ==> It removes the last inserted item
           #Syntax :-    d.popitem()
 5.del      ==> It removes item with the specified key
          #Syntax :-    del d[key]
 6.clear()  ==> It empties the dictionary
           #Syntax :- d.clear()

Python 3.9.9 (tags/v3.9.9:ccb0e6a, Nov 15 2021, 18:08:50) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #How to find the index of given substring in string?
>>> #How to replace the substring with another substring in string?
>>> #index() ==>Returns the position of substring
>>> #syntax :- 1. variablename.index(substring)
>>> #2.variable_name.index(substring,starting position)
>>> #3.variable_name.index(substring,start,endpositon)
>>> #replace()==>Returns a string where a specified value is replaced with a specifed value
>>> #syntax :- variable_name.replace(old,new,count)
>>> #old ==> old substring u want to replace
>>> #new ==> new substring which would replace the old string>>> #count==> (Optional) the no.of.times u want to repalce the old substring with ne"""
"""
con=1
n=10
while(con<n):
        print(con)
        con=con+1

"""
"""
con=1
n=10
while(con<n):
         if(con==5):
             break
         print(con)
         con=con+1
"""
"""con=1
n=10
while(con<n):
     if(con==5):
             con=con+1
             continue       
     print(con)
     con=con+"""
"""
a=10
b=20
c=(a+b)/2
print(c)
a=30
b=40
c=(a+b)/2
print(c)
a=21
b=90
c=(a+b)/2
print(c)

"""
"""
Lambda Function:

       Another name of the Lambda function is Anonymous function.

       An anonymous function in Python is one that has no name
when it is defined.
       
       The lambda keyword is used to define the functions rather than
the def keyword, which is used for normal functions.

      Anonymous functions can accept multiple inputs and return one output.
They can contain only a single executable statement.

      The scope of the parameters of an anonymous method is
the anonymous-method-block.

       An anonymous method can use generic parameter types like any other
method.

       Anonymous function cant be used anywhere outside.
       
      Syntax  :    lambda [args] : expression
      
#1. By lambda Function

num=10
fun=lambda a: a*10
r=fun(num) #function call
print(r)

#2. By Normal Function

def  add_plus_one(num) : #function definition
        return num*10
num=10
r=add_plus_one(num) #function call
print(r)
"""

"""
MODULES
"""
class Student:
        def __init__(key,a,b):
                key.name=a
                key.age=b
        def __str__(key):
                return f"{key.name} {key.age}"

def add(a,b):
        return a+b
a=[10,20,30,40,50]
b={1:"Apple",2:"Mango",3:"Banana"}



      

      
       















          
     
