"""
A python program to counting the number of legs and heads for rabit(x) and Hen(y)

ex:
input:heads=35,legs=110
output:x=20 and y=15
"""
heads=int(input("Enter the numbers of heads"))
legs=int(input("Enter the numbers of legs"))
x=(legs//2)-heads #number of four legs animals
y=heads-x #number of two legs animals
print("No.of Four leg animals",x)
print("No.of Two leg birds",y)
