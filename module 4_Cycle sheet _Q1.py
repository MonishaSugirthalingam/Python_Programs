"""
AIM  :  Pythan program to determine if there exists an elements in the list such that the sum of the elements on its left is equal to the sum of the elements on its right
"""
n=int(input("Enter the length of list"))
List=[]
List1=[]
# add the items in List
elements=input("Enter a elements")
for i in elements:
    if i.isdigit():
         List.append(int(i))
# To find sum of the items in List     
for j in range(len(List)):
    a=sum(List[j+1:])
    b=sum(List[:j])
# if its left sum as same as right,its append in List1 with there index value otherwise append in List1 with number '0'    
    if a==b:
        List1.append(j)
    else:
        List1.append(0)    
#Then find the item in List1 which is not equal to '0'.which means is zero there sum is not equal        
for k in range(len(List1)):
    if List1[k]!=0 :
        print(k)
if sum(List1)==0:
    print("0")
