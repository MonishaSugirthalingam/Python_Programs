#To find the given number is palyndrome or not
"""
INPUT:
1661
OUTPUT:
The number is polyndrome
"""
n1=str(int(input("Enter a number : ")))
n2=n1[::-1]
if n1==n2:
    print("The number is polyndrome")
else:
    print("Not polyndrome")
