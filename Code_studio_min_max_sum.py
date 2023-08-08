"""
EX:
INPUT:
2
5
3 3 3 3 3 
1
-1
Output:
6
-2
"""
def sumOfMaxMin(arr):
    a=max(arr)
    b=min(arr)
    return a+b
sum=[]
t=int(input())
for i in range(t):
    length=int(input())
    arr=list(map(int,input().split()))
    sum.append(sumOfMaxMin(arr))
for i in sum:
    print(i)
