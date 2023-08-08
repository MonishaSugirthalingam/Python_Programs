loop=int(input())
for times in range(loop):
    n=int(input())
    List=[]
    List1=[]
    result1=[]
    result2=[]
    elements=input()
    elements2=input()
    for i in elements:
        if i.isdigit():
            List.append(int(i))
    for j in range(len(List)):
        a=sum(List[j+1:])
        b=sum(List[:j])
        if a==b:
            List1.append(j)
            print(j)
        else:
            List1.append(0) 
    for k in range(len(List1)):
        if List1[k]!=0 :
            result1.append(k)
    print(result1)
    List2=[]
    List4=[]
    for i in elements2:
        if i.isdigit():
            List2.append(int(i))
    for j in range(len(List)):
        a=sum(List2[j+1:])
        b=sum(List2[:j])
        if a==b:
            List4.append(j)
        else:
            List4.append(0)    
    for k in range(len(List4)):
        if List4[k]!=0 :
            result2.append(k)
    print(result2)
    if  result1[0]==result2[0]:
        print(result[0])
