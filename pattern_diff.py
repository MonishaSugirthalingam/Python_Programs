a=input()
dict1={}
count=1
for i in range(65,91):
    b=chr(i)
    dict1[b]=count
    count=count+1
n=dict1.get(a)
for i in range(n):
    for j in range(1+i):
        print(j+1,end=" ")
    print()
