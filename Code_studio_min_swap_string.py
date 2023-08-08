"""
AIM  : Minimum operation needed to convert to the given string
EX :
INPUT                   OUTPUT
    1
    IFDfxPCdNvCNXPe      14
    NFfPICxeCNDdXPv

    2                     1
    ABC                
    ACB                  
    AbcD                  2
    bcAD
"""
def swap(str1,p,q):
    print(p,q)
    for i in range(len(str1)):
        for j in str1[(i+1):]:
            if str1[i]==p and j==q:
                str1[i],str1[str1.index(j)]=str1[str1.index(j)],str1[i]
                print(str1)
    return str1
def checking(str1,str2):
    count=0
    for i in range(len(str2)):
        if str2[i]==str1[i]:
            count=count+1
            pass
        if len(str1)!=count and str2[i]!=str1[i]:
            return "continue"
        if count==len(str1):
            return "stop"
    count=0
x=0
check=""
n=int(input())
for i in range(n):
    str1=list(input())
    str2=list(input())
    while x>=0:
        if str1[x]==str2[x]:
            pass
        else:
            re=swap(str1,str1[x],str2[x])
            check=checking(re,str2)
        if check=="stop":
            break
        else:
            x=x+1
    print(x-1)
