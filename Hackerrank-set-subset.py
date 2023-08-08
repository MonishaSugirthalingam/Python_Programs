"""
To find subset
Input:
3 //no.of.loop
5 //len
1 2 3 5 6
9  //len
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Output:
True 
False
False
"""
loop=int(input())
box=[]
for i in range(loop):
    length1=int(input())
    s1=set(map(int,input().split()))
    length2=int(input())
    s2=set(map(int,input().split()))
    if(s1<=s2):
        box.append(True)
    else:
        box.append(False)
for i in box:
    print(i)

"""
To find Superset
Input
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78 ///SETA
2  //loops
1 2 3 4 5  //other sets
100 11 12
output:
False
""
setA=set(map(int,input().split()))
box=[]
loop=int(input())
for i in range(loop):
    sets=set(map(int,input().split()))
    if(setA>=sets):
        box.append(True)
    else:
        box.append(False)
if False not in box:
    print(True)
else:
    print(False)
