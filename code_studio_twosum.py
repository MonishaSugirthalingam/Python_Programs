"""
INPUT:
2
4 9
2 7 11 13
5 1
1 -1 -1 2 2
OUTPUT:
2 7
-1 2
-1 2
"""
def summing(arr,s):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            if (arr[i]+arr[j])==s:
                print(arr[i],arr[j])
n=int(input())
for i in range(n):
    ele,sums=input().split()
    inputs=list(map(int,input().split()))
    summing(inputs,int(sums))
