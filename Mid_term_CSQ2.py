import math
List=[]
a=int(input())
for i in range(a):
    b=int(input())
    List.append(b)
if len(List)%2==1:
    mid=statistic.median(List)
    x=List.index(mid)
    for i in List[:x]:
        if mid>i:
            continue
        else:
            print("No Number having a Mid property")
    for j in List[x:]:
        if mid<i:
            continue
        else:
            print("No Number having a Mid property")
    print(list(mid))      
else:
    print("No number having mid property")
