n=int(input("Enter the number :"))
box=[]
for i in range(1,n):
    if n%i==0:
        box.append(i)
if sum(box)==n:
    print("The given number is perfect")
else:
    print("Its not a perfect number")
