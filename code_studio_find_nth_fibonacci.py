def fibonacciNumber(n):
   if n==1:
    return 1
   elif n==2:
        return 1
   else:
        return fibonacciNumber(n-1)+fibonacciNumber(n-2)
n=int(input())
for i in range(n):
    num=int(input())
    print(fibonacciNumber(num))
    print()
