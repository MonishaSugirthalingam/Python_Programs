"""
Input:
3
odd 2
even 3
odd 5
Output:
1
3
0
2
4
1
3
5
7
9
"""
n=int(input())
empty=[]
i=0
result=[]
for j in range(n):
    condition,times=input().split()
    if condition=="odd":
        while(len(empty)<int(times)):
            if i%2==1:
                empty.append(i)
            i=i+1
        c=empty.copy()
        result.append(c)
        empty.clear()
        i=0
    if condition=="even":
        while(len(empty)<int(times)):
            if i%2==0:
                empty.append(i)
            i=i+1
        c=empty.copy()
        result.append(c)
        empty.clear()
        i=0
for m in result:
    for n in m:
        print(n)
