r=1 
s=2
n=int(input())
p=1 
q=2
a=1 
b=2
c=1 
d=2
count=count1=count2=0
for I in range(1,n):
    for j in range(I,n+1):
        print(" ",end=" ")
    if I%2==1:
        if I>1:
            p=1 
        for j in range(I-1):
            print(p,end=" ")
            p=p+2
    if I%2==0:
        if I>2:
            q=2
        for j in range(I-1):
            print(q,end=" ")
            q=q+2
    if I%2==1:
        if I>1:
            count=count+1
            x=count*2
            r=I+x 
        for j in range(I):
            print(r,end=" ")
            r=r-2
    if I%2==0:
        if I>=2:
            count1=count1+1
            y=count1*2
            s=I+y
        for j in range(I):
            print(s,end=" ")
            s=s-2
    print()
for I in range(n,0,-1):
    for j in range((n+1)-I):
        print(" ",end=" ")
    if I%2==1:
        count=count+1
        if count>1:
            a=1 
        for j in range(I-1):
            print(a,end=" ")
            a=a+2
    if I%2==0:
        count1=count1+1
        if count1>1:
            b=2
        for j in range(I-1):
            print(b,end=" ")
            b=b+2
    count2=count2+1
    if I%2==1:
        c=I+4
        if count2>1:
            c=c-2
            if c==3:
                c=1
        for j in range(I):
            print(c,end=" ")
            c=c-2
    if I%2==0:
        d=I*2
        for j in range(I):
            print(d,end=" ")
            d=d-2
    print()    
            
