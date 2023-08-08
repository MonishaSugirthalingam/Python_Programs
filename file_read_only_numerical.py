file_name=input()
fq=open(file_name,"r")
s=fq.readlines()
fq.close()
import re
count=0
b=[]
for i in s:
    a=re.findall(r"\b[0-9]+\b",i)
    b=b+a
for i in b:
    print(int(i))
    
