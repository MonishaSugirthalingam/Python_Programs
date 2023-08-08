N=int(input())
E=input()
p=[]
q=[]
r=[]
list_of_points=[]
for i in E:
    if i.isdigit():
        p.append(int(i))
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
n1=tuple(str(len(list_of_points)))
n=str(n1)
N1=n.replace("'","")
N2=N1.replace(",","")
if len(list_of_points)!=0:
    print("Count Inversion",end=" ")
    print(N2,end=" ")
    print("-",end=" ")
    print(list_of_points)
else: 
    print("Count Inversion",end=" ")
    print(N2)
    
maximum=max(p)
minimum=p[-1]
maxmin=[]
maxmin.append(maximum)
maxmin.append(minimum)
if maximum==minimum:
    maxmin.remove(minimum)
M=tuple(str(len(maxmin)))
m=str(M)
M1=m.replace("'","")
M2=M1.replace(",","")

print("Leader",end=" ")
print(M2,end=" ")
print("-",end=" ")
print(maxmin)
