"""
AIM:python program to find the given password valid or not
"""
import re
P=input("Enter a password : ")
if len(P)>6 and len(P)<16:
    f=re.compile(r"\b[a-z].+[A-Z].+[0-9].+[\$@#]+\b")
    for x in re.findall(f,P):
        if x:
            print("The given password %s valid"%(P))
        else:
            print("The given password %s Invalid"%(P))
else:
    print("The given password %s Invalid"%(P))
