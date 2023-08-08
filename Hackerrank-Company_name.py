s="qwertyuiopasdfghjklzxcvbnm"
unique=[]
occ=[] 
re=[]
y=[]
def result(unique,re):
    for i in re:
        print(i,s.count(i))
for i in s:
    if i not in unique:
        unique.append(i)  
for i in unique:
    count=s.count(i)
    occ.append(count)
occ1=occ.copy()
unique1=unique.copy()
for i in occ:
    if occ.count(i)==1:
        re.append(unique[occ.index(i)])
if len(re)==0:
    unique.sort()
    result(unique,unique[0:3])
else:
    for i in range(len(unique)):
        for j in re:
            if unique[i]==j:
                unique1.remove(j)
                occ1.remove(s.count(unique[i]))
    a=[]
    for i in occ1:
        if i not in a:
            a.append(i)
    for i in range(len(a)):
        for j in range(len(occ1)):
            if a[i]==occ1[j]:
                x=ord(unique[j])
                y.append(x)

        p=min(y)
        q=chr(p)
        re.append(q)
        y.clear()
    result(unique,re[0:3])
                
           
