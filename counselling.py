"""
A python program to short the students details so that it will be convinet to call for counselling
Ex:
input name,address,mark
output:short the list

"""
a=[]
b=[]
c=[]
c1=[]
shorted_list={}
x={}
try:
    user=True
    while True:
        name=input("Enter the name of the student")
        add=input("Enter the address if the student")
        mark=int(input("Enter the score"))
        a.append(name)
        b.append(add)
        c.append(mark)
       
except ValueError:
    user=False
c1.extend(c)     
def bubble_short(c):
    for i in range(len(c)-1,0,-1):
        for j in range(i):
            if c[j]<c[j+1]:
                c[j],c[j+1]=c[j+1],c[j]
                
    
bubble_short(c)
for i in c:
    x[i]=c1.index(i)
y=x.values()
z=x.keys()
count=0
for val in y:
    m=a[val]
    n=b[val]
    o=z[count]
    shorted_list[m]=(m,o,n)
    count=count+1
s=input("if you want to saw the entire list,please press no 1 else press 2")
if s==1:
    d=shorted_list.values()
    for i in d:
        print(i)
else:
    print(shorted_list)
    


