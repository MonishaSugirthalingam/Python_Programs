def func(a,b):
    XOR=[]
    for i in range(len(a)):
        if (a[i]=="0" and b[i]=="0") or (a[i]=="1" and b[i]=="1"):
            XOR.append("0")
        if (a[i]=="0" and b[i]=="1") or (a[i]=="1" and b[i]=="0"):
            XOR.append("1")
    return XOR
string1=input()
string2=input()
print("".join(func(string1,string2)))
