a=[]
b=[]
for i in range(7):
    LIST=["fox","corn","goose","nothing"]
    List1=["fox","corn","goose"]
    print(LIST)
    senario1=input("choose any one from the list and cross the river")
    print("Which direction we want to go ?")
    List2=["East_to_West,West_to_East"]
    flag=0
    print(List2)
    Direction1=int(input("if you want east_to_west please press'2' or if you want west_to_east please select'1' "))
    if Direction1==1 :
        if senario1=="nothing":
            b.append(senario1)
        if senario1!="nothing" and Direction1==1:
            List1.remove(senario1)
            print(List1)
            a.append(senario1)
            print(a)
            
    if Direction1==2:
        if senario1=="nothing":
            b.append(senario1)
        if senario1!="nothing" and Direction1==1:
            List1.append(senario1)
            print(List1)
            a.remove(senario1)
            print(a)
    if Direction1==1 :        
        for i in a:
            if i=="goose":
                continue
            if i=="fox":
                print("not safe")
                flag=1
                break
            if i=="goose":
                continue
            if i=="corn":
                print("not safe")
                Flag=1
                break
        if len(List1)==2:
               if (List1[0]=="goose" and List1[1]=="fox") or (List1[1]=="goose" and List1[0]=="fox") :
                    print("not safe")
                    Flag=1 
                    break
                
               if (List1[0]=="goose" and List1[1]=="corn") or (List1[1]=="goose" and List1[0]=="corn") :
                    print("not safe")
                    Flag=1 
                    break
    if Direction1==2 :        
        for i in a:
            if i=="goose":
                continue
            if i=="fox":
                print("not safe")
                flag=1
                break
            if i=="goose":
                continue
            if i=="corn":
                print("not safe")
                Flag=1
                break
        if len(List1)==2:
               if (List1[0]=="goose" and List1[1]=="fox") or (List1[1]=="goose" and List1[0]=="fox") :
                    print("not safe")
                    Flag=1 
                    break
                
               if (List1[0]=="goose" and List1[1]=="corn") or (List1[1]=="goose" and List1[0]=="corn") :
                    print("not safe")
                    Flag=1 
                    break
                
    
    if flag==1:
        break
if flag!=1 :
    print("You are successfully cross the river")
