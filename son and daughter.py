List_from_daugter=set()
List_from_son=set()
item1=int(input("How many items she want to bye"))
item2=int(input("How many items he want to bye"))
for i in range(item1):
    item=input("Enter Name of the item which is she want to bye")
    List_from_daugter.add(item)
for i in range(item2):
    item=input("Enter name of the item which is he want to bye")
    List_from_son.add(item)
List=List_from_daugter|List_from_son
print("This the list which are bought by father",List)
