# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
n=int(input())
d={}
d=OrderedDict()
for i in range(n):
    read=input()
    s=""
    sums=""
    for i in range(len(read)):
        if(read[i].isalpha() or (read[i]==" " and read[i+1].isalpha())):
            s=s+read[i]
        if(read[i].isdigit()):
            sums=sums+read[i]
    if(len(d)>0):
            t1=d.keys()
            if s in t1:
                d[s]=d.get(s)+int(sums)
            else:
                d[s]=int(sums)
    else:
            d[s]=int(sums)
val=d.values()
key=d.keys()
for i in key:
    print(i,end=" ")
    print(d.get(i))
