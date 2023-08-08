"""
Input
2 3 4 5
0 1 2 3
0 2 3 4
output:
0
4
1
"""
n=input().split()
a=int(n[0])
found=""
count=0
while count<a:
    count=count+1
    if str(count) not in n:
        found=found.join("Yes")
        n.insert(0,str(count))
        break
if found=="":
    while True:
        a=a+1
        if str(a) not in n:
            n.insert(0,str(a))
            break
print("".join(n))


