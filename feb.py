m=input()
n=input()
set1_all_numbers=[]
set2_all_numbers=[]
set3_all_numbers=[]
for i in m:
    a=int(i)
    set1_all_numbers.append(a)
for j in n:
    b=int(j)
    set1_all_numbers.append(b)
for i in set1_all_numbers:
    a=1
    b=1
    c=0
    if i==0 or i==1:
        set2_all_numbers.append(i)
    else:
        while c<i:
            c=a+b
            b=a
            a=c
            if c==n:
                set2_all_numbers.append(i)
for i in set1_all_numbers:
    if i>1:
        for j in range(2,int(i/2)+1):
            if i%j==0:
                pass
            else:
                set3_all_numbers.append(i)
x=set(set1_all_numbers)
y=set(set2_all_numbers)
z=set(set3_all_numbers)
print((x|y)&z)
print(x&y)
print(x&z)

    
