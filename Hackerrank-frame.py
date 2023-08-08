"""
Input:
Size of the pattern  3(like 3,4,5,6...)
output:
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----
"""
n=int(input("Enter the size of the pattern :"))
alphas=[]
count1=count=0
while count<n:
    alphas.append(chr(count+97))
    if count==n-1:
        break
    alphas.append("-")
    count=count+1
alpha=alphas[::-1]
count=count1=count2=count3=1
for i in range(n-1):
    for j in range(n-(i+1)):
        print("-"*2,end="")
    for j in range(count):
        print(alpha[j],end="")
    count=count+2
    a=alpha[:(count1-1)]
    for j in a[::-1]:
        print(j,end="")
    count1=count1+2
    for j in range(n-(i+1)):
        print("-"*2,end="")
    print()
for i in range(n):
    for j in range(i):
        print("-"*2,end="")
    for j in range((len(alpha)-count2)+1):
        print(alpha[j],end="")
    count2=count2+2
    b=alpha[:((len(alpha)-count3))]
    for j in b[::-1]:
        print(j,end="")
    count3=count3+2
    for j in range(i):
         print("-"*2,end="")
    print()
    
        
