"""
INPUT:
2
4 2
90 45 67 213
5 1
78 12 4 6 8
OUTPUT:
213
90
78
"""
def Klargest(a, k):
    n=[]
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
    for i in range(k):
        n.append(a[i])
    return n
result=[]
n=int(input())
for i in range(n):
    length,k=input().split()
    a=list(map(int,input().split()))
    result.append(Klargest(a,int(k)))
for i in result:
    for j in i:
        if j!=None:
            print(j)
