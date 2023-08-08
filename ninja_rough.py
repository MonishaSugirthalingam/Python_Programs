def missingnum(a):
    b=a[0]
    if str(b).isdigit():
        while b<=0:
            b=b+1
            if b not in a:
                print(b)
                break
     
n=int(input())
for i in range(n):
    length=input()
    num=input().split()
    def typeschange(num):
        for i in num:
            num[num.index(i)]=int(i)
        return num    
    num=typeschange(num)
   
    missingnum(num)
    
