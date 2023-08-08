length=int(input("Enter the length of the list"))
n=input("Enter the RPN form")
m=n.split()
k=[]
for i in m:
    if i.isdigit():
        k.append(i)
    else:
        a=k[::-1]
        if i=="+":
            z=int(a[1])+int(a[0])
        if i=="-":
            z=int(a[1])-int(a[0])
        if i=="*":
            z=float(a[1])*float(a[0])
        if i=="/":
            z=int(a[1])/int(a[0])
        k.remove(a[1])
        k.remove(a[0])
        k.insert(0,z)
        k=k[::-1]
print(int(k[0]))
