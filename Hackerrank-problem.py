"""
AIM :If there are symbols or spaces between two alphanumeric characters of the decoded script, then Neo replaces them with a single space '' for better readability.
Input:
7 3
Tsi
h%x
i #
sM 
$a 
#t%
ir!
Output:
This is Matrix#  %!
"""
box=[]
row,col=input().split()
for i in range(int(row)):
    box.append(input())
box1=[]
for k in range(int(col)):
    for i in box:
        box1.append(i[k])
import re
s="".join(box1)
x=re.findall("[a-zA-z][@#%$!*^? ]+[a-zA-Z]",s)
re=[]
empty=[]
for i in x:
    for j in i:
        if j.isalpha():
            empty.append(j)
    empty.insert(1," ")
    re.append("".join(empty))
    empty.clear()
for i in range(len(x)):
    a=x[i]
    b=re[i]
    c=re.sub("a","b",s)
    print(c)
        
        
        
