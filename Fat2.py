string=input()
dict1={}
s=string.split()
s.sort()
for i in s:
    c=s.count(i)
    if i not in l:
        dict1[l]=c
print(dict1)
       
