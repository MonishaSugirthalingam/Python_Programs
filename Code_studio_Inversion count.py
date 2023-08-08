def tofindinversion(List):
    count=0
    for i in range(len(List)):
        for j in range(i,len(List)):
            if List[i]>List[j]:
                count=count+1
               
    return count
print(tofindinversion(list(map(int,input().split()))))
