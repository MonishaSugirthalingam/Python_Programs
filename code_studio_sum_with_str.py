n=int(input())
for i in range(n):
    num1=input().split()
    num2=input().split()
    del num1[-1]
    del num2[-1]
    num1=int("".join(num1))
    num2=int("".join(num2))
    add=list(str(num1+num2)+"-1")
    for i in range(len(add)):
        if add[i]=="-":
            print(add[i]+add[i+1])
            break
        print(add[i],end=" ")
    print()
    
