"""
Example:
INPUT:
2        //length of list
5        // length of list m
["john","smith",1234,"B+",10.03]      // actual row
["jokcky","jr",6789,"A+",40.03]       //actual list row2
2       // index of the primary key
1234    // value of the primary key query

OUTPUT:
["john","smith",1234,"B+",10.03] 
"""
row1=[]
row2=[]
row=int(input("Enter a number of rows"))
length=int(input("Enter a length of the list"))
for i in range(row):
    if len(row1)!=5 and len(row1)==0:
        while len(row1)<length:
            r1=input("Enter a elements in row1")
            row1.append(r1)
    else:
        while len(row2)<length:
            r2=input("Enter a elements in row2")
            row2.append(r2)
A=int(input("Enter a index of the primary key"))
B=input(" Enter avalue of the primary key query")
if row1[A]==B:
    print(row1)
if row2[A]==B:
    print(row2)    
