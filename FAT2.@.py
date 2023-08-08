
import re
string=input().lower() #read the string
num=re.findall(r"[@#%$*&/?!]",string) #seperate the special charactors
for i in num:
    d=re.search(i,string)
    g=d.start()
if len(num)>1 and g==len(string)-1:
    print("Invalid input") #if special charactors occurs more than one ,display invalid
elif len(num)==1: 
    s1=re.sub(r"[^a-zA-Z0-9]"," ",string)# to find the letters ,without  special charactors
    dict1={}
    l=[]
    acc=[]
    s=s1.split() #split the string respected to the space
    s.sort() # sort the list
    for i in s:
        c=s.count(i)
        if i not in l:
            l.append(i)
            acc.append(c)
    count=0
    for i in l:
        dict1[i]=int(acc[count])
        count=count+1
    print(dict1) #display the letters with no.of occurance


