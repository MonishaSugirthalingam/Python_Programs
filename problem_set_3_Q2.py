bucket_size=int(input())
empty=[] 
original=[]
for i in range(bucket_size):
    empty.append(i)
    Name=input()
    original.append(Name)
for i in original:
    occ=ord(i[0])%bucket_size
    if type(empty[occ])==str:
        s=[]
        for k in empty[occ:]:
            s.append(type(k))       
        if  int not  in s or  occ==bucket_size-1:
            occ=0
           
        for j in empty[occ:]:
            if type(j)==int :
                empty[empty.index(j)]=i
                break
    
    else:
        empty[occ]=i 
print(empty)
def reverse_name(name,a):
    if a==0:
        return name[a]
    else:
        return name[a]+reverse_name(name,a-1)
def order(empty):
    list_of_reversed=[]
    for i in empty:
        length=len(i)-1
        list_of_reversed.append(reverse_name(i,length))
    return list_of_reversed     
print(order(empty))
        
    
