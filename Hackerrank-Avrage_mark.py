"""
INPUT:
3
MONI 56 67 78
KANI 56 78 90
BANU 23 12 56
BANU
OUTPUT:
30.33
"""
n=int(input())
dict1={}
import re
for i in range(n):
    a=input()
    b=re.findall("[a-zA-Z]+",a)
    c=re.findall("([0-9]+[.?0-9]+|\d+)",a)
    dict1[b[0]]=c
e=input()
s=dict1.get(e)
total=0
for i in s:
    total=total+int(i)
print("{:.2f}".format(total/len(s)))
