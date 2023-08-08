"""
INPUT:
5     \\number of students
herry  \\ name of the student
37.21   \\ mark
berry
37.21
tina
37.2
apple
41
harsf
39
OUTPUT:
berry
herry
"""
n=int(input())
p=[]
q=[]
result=[]
for i in range(n):
    name=input()
    score=float(input())
    p.append(score)
    q.append(name)
a=p.copy()
b=min(a)
for i in a:
    if i!=b :
        result.append(i)
c=min(result)
final=[]
for i in range(len(p)):
    if p[i]==c:
        final.append(q[i])
final.sort()
for i in final:
    print(i)

    
