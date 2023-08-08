#To find the given number is ARMSTRONG number or not
"""
INPUT:
153
OUTPUT:
"The given number is ARMSTRONG"
"""
n=str(int(input("Enter a number :")))
multy=len(n)
result=[]
for i in range(len(n)):
    s=int(n[i])**multy
    result.append(s)
if sum(result)==int(n):
    print("The given number is ARMSTRONG")
else:
    print("Not ARMSTRONG")
