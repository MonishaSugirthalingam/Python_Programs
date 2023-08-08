a=[]
try:
    value=True
    while True:
        n=int(input("Enter a element"))
        a.append(n)
except ValueError:
    value=False
if len(a)%2==1:
    a.remove(a[0])
    a.remove(a[-1])
    b=len(a)
    mid=a[(0+b)//2]
    x=a[:a.index(mid)]
    y=a[(a.index(mid))+1:]
    for i in x:
        if i<mid:
            found=True
        else:
            print("No number having mid point")

    for j in y:
        if j>mid:
            found=True
        else:
             print("No number having mid point")
    if found==True:
        print(mid)
else:
    print("No number having mid point")
            
