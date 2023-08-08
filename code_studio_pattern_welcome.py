"""
INPUT:
Example:
7 0r 11 or 9      \\length of the frame should be a odd number
21 or 33 or 27     \\breath of the frame  should be 3 times of length
WELCOME or MONISHA  \\ length of the name should be a odd number
"""
print("length of the frame should be a odd number")
n=int(input("Enter the length of the frame :"))
print("breath of the frame  should be 3 times of length")
m=int(input("Enter the breath of the frame :"))
print("length of the name should be a odd number")
pattern=input("Enter your Sweet Name :")
length=len(pattern)
print("This is the frame for you!!!!!")
p=(n-1)//2
q=(m-3)//2
for i in range(p):
    if i>=1:
        k=k+3
    else:
        k=0
    for j in range(k,q):
        print("-",end="")
    if i>=1:
        x=x+3
    else:
        x=2
    for j in range(x):
        if j>=1 and (j-1)%3==0:
            print("|",end="")
        else:
            print(".",end="")
    if i>=1:
        y=y+3
    else:
        y=2
    for j in range(y-1):
        if j>=2 and (j+1)%3==0:
            print("|",end="")
        else:
            print(".",end="")
    if i>=1:
        L=L+3
    else:
        L=0
    for j in range(L,q):
        print("-",end="")
    print()
r=(m-length)//2
for i in range(1):
    for j in range(r):
        print("-",end="")
    for j in range(length):
        print(pattern[j],end="")
    for j in range(r):
        print("-",end="")
    print()
for i in range(p):
    if i>=1:
        k=k+3
    else:
        k=3
    for j in range(k):
        print("-",end="")
    for j in range((q-k)+2):
        if j>=1 and (j-1)%3==0:
            print("|",end="")
        else:
            print(".",end="")
    for j in range(((q-k)+2)-1):
        if j>=2 and (j+1)%3==0:
            print("|",end="")
        else:
            print(".",end="")
    if i>=1:
        L=L+3
    else:
        L=3
    for j in range(L):
        print("-",end="")
    print()
    
