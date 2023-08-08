section1=[]
section2=[]
while True:
    items_in_sec1=input("Add the items in section 1")
    section1.append(items_in_sec1)
    stop1=input("If you want to stop to store items in section1,please will press the 'yes',otherwise we will press any key")
    if stop1=="yes":
        break
while True:    
    items_in_sec2=input("add the items in section 2")
    section2.append(items_in_sec2)
    stop2=input("If you want to stop to store items in section2,please will press the 'yes',otherwise we will press any key")
    if stop2=="yes":
        break
section1.sort()
section2.sort()
section1.extend(section2)
for things in section1:
    section1.count(things)
    if section1.count(things)!=1:
        section1.remove(things)
        print(list(section1))   
    
