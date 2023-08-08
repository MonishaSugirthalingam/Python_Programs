def bubblesort(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a 
n=int(input())
for i in range(n):
    length=int(input())
    a=input().split()
    s=bubblesort(a)
    for i in s:
        print(int(i),end=" ")
    print()
