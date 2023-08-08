n=int(input())

def sums(a):
    if a==0:
        return 0 
    else:
        return a+sums(a-1)
def product(a):
    if a==0:
        return 1 
    else:
        return a*product(a-1)
s=[]
for i in range(n):
    num=input()
    val=num.split()
    s.extend(val)
for i in s:    
    if int(i[0])==1:
        print(sums(int(val[0])))
    if int(i[0])==2:
        print(product(int(val[0])))
    
