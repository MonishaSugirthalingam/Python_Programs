n=input()
point=1
name=[]
points=[]
j=0
for i in range(len(n)):
    j=i-j
    if n[j]==n[j+1] and n.count(n[j])>1:
        point=point+1
    elif n.count(n[j])==1:
        point=1
        points.append(point)
        name.append(n[j])
    else:
        points.append(point)
        name.append(n[j])
        point=1
print(points)
print(name)

        
    
    
