def funcsum(List,sums):
    result=[]
    for i in List:
        for j in range(len(List)-1):
            if int(i)+int(List[j])==int(sums):
               
    return result
n=int(input())
for i in range(n):
    length,sums=input().split()
    List=input().split()
    print(funcsum(List,sums))
