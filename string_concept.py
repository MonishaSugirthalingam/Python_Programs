n="123"
if n.isalnum():
    print(True)
else:
    print(False)
count1=count2=count3=count4=0
for i in range(len(n)):
    if n[i].isalpha():
        count1=1
    if n[i].isdigit():
        count2=1
    if n[i].islower():
        count3=1 
    if n[i].isupper():
        count4=1
if count1==1:
    print(True)
else:
    print(False)
if count2==1:
    print(True)
else:
    print(False)
if count3==1:
    print(True)
else:
    print(False)
if count4==1:
    print(True)
else:
    print(False)

    

