"""
input:
8  \\ first list
listen
tow
silent
lisent
two
abc
no
on
4  \\second list
two
bca
no
listen
output:  \\ whch are have a same letters 
2
1
2
3
"""

n1=int(input())
dict1=[]
for i in range(n1):
    str1=input()
    dict1.append(str1)
n2=int(input())
query=[]
for i in range(n2):
    str2=input()
    query.append(str2)
result=[]
a=[]
b=[]
count=0
for i in query:
    i=list(i)
    for j in dict1:
        j=list(j)
        for letter in i:
            if letter not in j:
                a.append("no")
        if "no" not in a:
            b.append(a)
        a.clear()
    print(len(b))
    b.clear()    
                
            
        
    
        
