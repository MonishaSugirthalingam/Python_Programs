"""
Input:
2     //No of tuples
7     //No of items in 1st tuple
Education    //Items  in the 1st tuple catagory
Primary     // Component
50         //cost
Secondary
25
Higher 20
7            //No of items in 2nd tuple
Defense      //Items in the 2nd tuple     Category
Army        //Component
25             //Cost
AirForce
40
Navy
45
Output:
((Education, 95), (Defense, 110))
"""
E={}
d=[]
A=int(input("Enter a number tuples "))#No of tuples
for i in range(A):
    B=int(input("Enter a number items"))#No of items in 1st tuple
    C=input("Enter a catagory")#Items  in the 1st tuple catagory
    f=B-1
    f1=int(f/2)
    if f1<0:
        E[C]=0
        print(tuple(E.items()))
        break
    for j in range(f1):
        d1=(input("Enter a name of the items"))
        d2=int(input("Enter the cost of theitems"))#cost of the items append in list d
        d.append(d2)
        s=sum(d)#to find sum of the elements in list d
        E[C]=s# its save as dictionary called E
    d.clear()
    print()
print(tuple(E.items()))#Dictionary convert into tuple        
        
        
    
    
          
