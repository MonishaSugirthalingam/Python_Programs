"""
"""
message=input("Enter the message")
a=message.split()
x=[]
y=[]
length=len(a)//2
print(length)
for j in a:
    if len(x)<length:
        x.append(j)
    else:
        y.append(j)
x1=x[0]
y1=y[0]
x.remove(x1)
y.remove(y1)
import re
p=re.findall("^[0-9]{0,11}$",str(x))
q=re.findall("^[0-9]{0,11}$",str(y))


        
