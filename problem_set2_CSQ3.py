def Inversion(p,N):
    q=[]
    r=[]
    list_of_points=[]
    for i in p:
        k=p.index(i)
        w=k+1
        for j in range(N-k-1):
            if N-k-1==0:
                break
            if i>p[w]:
                q.append(i)
                r.append(p[w])
            w=w+1
    for i in range(len(q)):
        merge_list=q[i],r[i]
        list_of_points.append(merge_list)
    n1=tuple(str((len(list_of_points))))
    n=str(n1)
    N1=n.replace("'","")
    N2=N1.replace(",","")
    if len(list_of_points)==0:
        print("Count Inversion",end=" ")
        print(N2)
        
    else:
        print("Count Inversion",end=" ")
        print(N2,end=" ")
        print("-",end=" ")
        print(list_of_points)
    
    

def printLeaders(arr,size):
    l=[]
    c=[]
    count=0
    for i in range(0,size):
        for j in range(i+1,size):
            if arr[i]<=arr[j]:
                break
            elif j==size-1:
                count+=1
                l.append(arr[i])
    l.append(arr[size-1])
    if count==0:
        c.append(arr[size-1])
    else:
        c.append(count)
        c.append(arr[size-1])
    
    M=tuple(str(len(l)))
    m=str(M)
    M1=m.replace("'","")
    M2=M1.replace(",","")
    print("Leader",end=" ")
    print(M2,end=" ")
    print("-",end=" ")
    print(l)
                
                
n=int(input())
x=list(map(int,input().split()))
Inversion(x,n)
printLeaders(x,n)


