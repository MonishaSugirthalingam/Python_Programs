import re
opo=int(input())
result=[]
multiset=[]
for i in range(opo):
    fun=input()
    if re.findall("add",fun):
        a=re.findall("[0-9]+",fun)
        b=a[0]
        multiset.append(b)
    if fun=="size":
        result.append(len(multiset))
    if re.findall("query",fun):
        a=re.findall("[0-9]+",fun)
        b=a[0]
        if b in multiset:
            result.append("True")
        else:
            result.append("False")
    if re.findall("remove",fun):
        a=re.findall("[0-9]+",fun)
        b=a[0]
        multiset.remove(b)
for i in result:
    print(i)
