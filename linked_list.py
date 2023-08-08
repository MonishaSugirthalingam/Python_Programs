I1="[2,3,4]"
I2="[5,6,7]"
a=I1.replace("[","")
b=a.replace("]","")
p=b.replace(",","")
c=I2.replace("[","")
d=c.replace("]","")
q=d.replace(",","")
x=int(p[::-1])
y=int(q[::-1])
sums=str(x+y)
result=str(list(map(int,sums[::-1])))
print(result.replace(" ",""))
