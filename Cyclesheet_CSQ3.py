"""
AIM   :  a python program to list the students’ names who secured 
AUTHOR:  MONISHA.S 
DATE  :  26-12-2021
"""
dict1="abc:10,def:80,ijk:60"
import re
names=re.findall(r"\b[a-zA-Z]+\b",dict1)
scores=re.findall(r"\b[0-9]+\b",dict1)
def mean_score(names,score):
    for i in names:
        if scores.index(score)==names.index(i):
            name=i
    return(name)        
def findexact(Average,scores):
    exact_mean=[]
    for i in scores:
        if int(i)==Average or abs(int(i)-Average)<5:
            exact_mean.append(i)
    return exact_mean
sums=0
for i in scores:
    sums=sums+int(i)
Average=sums//len(scores)
exact_mean=findexact(Average,scores)
def sort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a
copy=scores.copy()
for i in exact_mean:
    if i in copy:
        copy.remove(i)
result=sort(copy)
score=exact_mean+result 
for i in score:
    print(mean_score(names,i))

