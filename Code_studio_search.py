"""
INPUT:
5      //length of list
1 2 3 4 5
3  //no of quires
8
7
2
OUTPUT:
-1  //8 is not in the list
-1
1    //1 is there so print that index
"""
def quries(arr,m):
    n=[]
    for i in m:
        if i in arr:
            n.append(arr.index(i))
        else:
            n.append(-1)
    return n
n=int(input())
arr=list(map(int,input().split()))
q=int(input())
m=[]
for i in range(q):
    m.append(int(input()))
    result=quries(arr,m)
for i in result:
    print(i)
