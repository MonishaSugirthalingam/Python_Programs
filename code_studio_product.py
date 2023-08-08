def resultfunc(arr,a):
 result=[]
 for i in arr:
    pro=1
    for j in range(a):
        if (arr.index(i)>j) or (arr.index(i)<j):
            pro=pro*int(arr[j])
    result.append(pro)
 return result
n=int(input())
s=[]
for i in range(n):
    length=int(input())
    arr=input().split()
    s.append(resultfunc(arr,length))
for i in s:
    for j in i:
        print(int(j),end=" ")
    print()
