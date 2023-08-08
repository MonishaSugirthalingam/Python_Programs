#To find the perfect number between 1 t0 10000
print("The perfect numbers are :")
def findfactorial(n):
    import math
    sum=0
    for i in str(n):
        sum=sum+math.factorial(int(i))
    q=sum
    sum=0
    if q==n:
        print(n)
for i in range(1,10000):
   findfactorial(i)
        
    
