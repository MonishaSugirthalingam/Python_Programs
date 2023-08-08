I1=input().split()
I2=input().split()
a=I1[::-1]
b=I2[::-1]
c=int("".join(a))
d=int("".join(b))
sums=str(c+d)
print(list(map(int,sums[::-1])))
