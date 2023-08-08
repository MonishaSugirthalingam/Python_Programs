"""
A python program to list the students name who secured
* exact mean score
*above mean score and
*below mean score

Ex:
input:
'siva':40,'kumar':60,'arun':80
output:
kumar
arun
siva
"""
dict1=input("Enter a list of students and marks: ")
import re
names=re.findall(r"\b[a-zA-Z]+\b",dict1)
scores=re.findall(r"\b[0-9]+\b",dict1)
def mean_score(names,score):
    for i in names:
        if scores.index(score)==names.index(i):
            name=i
    return(name)        
    
above_mean=(max(scores))
below_mean=(min(scores))
for i in scores:
    if i==above_mean or i==below_mean:
        pass
    else:
        exact_mean=i
print(mean_score(names,exact_mean))
print(mean_score(names,above_mean))
print(mean_score(names,below_mean))

