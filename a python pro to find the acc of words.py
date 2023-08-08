string=input("Enter a string").lower()
import re
s1=re.sub(r"[^a-zA-Z0-9]"," ",string)
dict1={}
l=[]
acc=[]
s=s1.split()
s.sort()
print(s)
for i in s:
    c=s.count(i)
    if i not in l:
        l.append(i)
        acc.append(c)
count=0
for i in l:
    dict1[i]=str(acc[count])
    count=count+1
print(dict1)
