team=input("Enter the name of the team :").upper()
name=input("Enter your name :").upper()
a=list(team.replace(" ",""))
b=name.replace(" ","")
box=[]
for i in range(len(b)):
    if (b[i] in a) and (b[i] not in box):
        box.append(b[i])
for i in range(len(box)):
    print(box[i],"-",1)

