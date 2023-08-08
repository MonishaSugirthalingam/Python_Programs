"""
Input:
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Output:
Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
"""
name=[]
result=[]
n=int(input("Enter the number of persons :"))
for i in range(n):
    details=input().split()
    name.append(details[0]+" "+details[1])
    if details[3]=="F":
        name.insert(0,"Ms. ")
    else:
        name.insert(0,"Mr. ")
    result.append("".join(name))
    name.clear()
for i in result:
    print(i)
        
