"""
AIM    :  A python program that defines a user-defined function called frequency () which identifies and count the frequency of occurrences of the words in a given sentence that is passed to the user defined function. 
AUTHOR :  MONISHA.S
DATE   :  26-12-2021 
"""
string=input()
l=[]
acc=[]
s=string.split()
s.sort()
for i in s:
    c=s.count(i)
    if i not in l:
        l.append(i)
        acc.append(c)
count=0
for i in l:
    print(i,"-",acc[count])
    count=count+1
    
