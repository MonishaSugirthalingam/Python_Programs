def reversing(List,m,n):
    for j in range(n):
        if j==m:
           List[j],List[j+1]=List[j+1],List[j]
    
    return List
n=int(input())
result=[]
for i in range(n):
    a=input()
    m=int(a[2])+1
    n=int(a[0])
    List=input().split()
    List=reversing(List,m,n)
    result.append(List)
    print(result)
for i in result:
    for j in i:
        print(int(j),end=" ")
    print()
    
    
