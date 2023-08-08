"""
Input:
1     \\no of test cases
3     \\len of the array
1 2 3  \\array
2       \\ no of query
1 3    \\sum between 1 to 3
1 5    \\ "    "    1 to 5
output:
6 9
"""
n=int(input())
def sumInRanges(arr,p,q):
    arrnew=arr*int(q)
    return sum(arrnew[int(p)-1:int(q)])
result=[]
for i in range(n):
    larr=int(input())
    arr=list(map(int,input().split()))
    lquery=int(input())
    for i in range(lquery):
        p,q=input().split()
        result.append(sumInRanges(arr,p,q))
    for i in result:
        print(i,end=" ")
    result.clear()
