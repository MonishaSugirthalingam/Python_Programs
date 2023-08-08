string=input()
a=b=0
for i in string:
    if (i.isalpha()):
        a=a+1
    if (i.isdigit()):
        b=b+1
print("no of digits: ",b)
print("no of alphabets : ",a)
            
