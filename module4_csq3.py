row1=[]
row2=[]
row=int(input())
length=int(input())
for i in range(row):
    if len(row1)!=5 and len(row1)==0:
        while len(row1)<length:
            r1=input()
            r1=r1.split()
            for i in r1:
                if i.isnumeric():
                    row1.append(int(i))
                else:
                    i='"'+i+'"'
                    row1.append((i))
    else:
        while len(row2)<length:
            r2=input()
            for i in r2:
                if i.isnumeric():
                    row2.append(int(i))
                else:
                    i='"'+i+'"'
                    row2.append((i))
A=int(input())
B=input()
if B.isdigit():
    B=int(B)
if row1[A]==B:
    for i in row1:
        if i==i.isalpha():
            i.strip("'")
        else:
            continue
    print(row1)
if row2[A]==B:
    for i in row2:
        if i==i.isalpha():
            i.strip("'")
        else:
            continue
    print(row2)    
