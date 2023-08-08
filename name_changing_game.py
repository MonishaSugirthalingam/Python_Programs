"""
INPUT:
Monisha
Output:
oih
mnsa
"""
name=input("Enter your name : ")
name1=list(name).copy()
nick1=[]
nick2=[]
for i in range(len(name)):
    if i%2==1:
        nick1.append(name[i])
        name1.remove(name[i])
    else:
        nick2.append(name[i])
        name1.remove(name[i])
print("".join(nick2))
