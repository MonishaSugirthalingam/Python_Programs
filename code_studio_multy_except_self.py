"""
2 \\input(test case)
3  \\len(input1)
1 2 3 \\lst
6 3 2 \\output
5     \\len(input2)
2 3 4 6 1  \\2nd
72 48 36 24 144  \\output
"""

def resultfunc(c):
    multy=1
    for i in range(len(c)):
        multy=multy*int(c[i])
    return multy
n=int(input())
result=[]
for i in range(n):
    length=int(input())
    arr=input().split()
    for i in range(len(arr)):
        a=arr[:i]
        if a==[]:
            a=a+["1"]
        b=arr[i+1:]
        if b==[]:
            b=b+["1"]
        c=a+b
        print(resultfunc(c),end=" ")
    print()
