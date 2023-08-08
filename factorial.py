list1=[]
list2=[]
for i in range(1,21):
    if i%2==0:
        list1.append(i)
print("Even numbers in the list")
print(list1)
for i in list1:
    f=1
    for j in range(1,i+1):
        f=f*j
    list2.append(f)
print("Factorial number of list1 values in list2")
print(list2)

print("After extending list2 to list1 even and factorials value in list")
list1.extend(list2)
print(list1)
