"""
Input:
EX1: a=[5,6,4,10]
     b=[4,6,10,5]
EX:2 a=[1,2,3]
     b=[1,3,2]
Output:
2
1
"""
a=[5,6,4,10]
b=[4,6,10,5]
count=0
def funswap(arr,p,q):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]==p and arr[j]==q:
                arr[i],arr[j]=arr[j],arr[i]
    return arr
def finding(re,a):
    count=0
    for i in range(len(a)):
        if a[i]==b[i]:
            count=count+1 
    if count==len(a):
       return "stop"
    else:
        return "continue"
    count=0
i=0
check=""
while i>=0:
    if b[i]==a[i]:
        pass
    else:
        re=funswap(b,b[i],a[i])
        check=finding(re,a)
    if check=="stop":
        break
    else:
        i=i+1
print(i-1)
      
    
