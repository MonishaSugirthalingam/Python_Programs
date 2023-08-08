"""
Input:
2   \\no of testcases
25   \\ testcase1  
45    \\ teastcase2
Output
0 1 2 3 4 5 6 7 8 9 10 12 21 23
0 1 2 3 4 5 6 7 8 9 10 12 21 23 32 34 43 
"""

def findJumpingNumbers(n):
    if n<=10:
        for i in range(n+1):
            print(i,end=" ")
    else:
        j=12
        for i in range(11):
            print(i,end=" ")
        while j<n:
            print(j,end=" ")
            j=int((str(j)[::-1]))
            if j<n:
                print(j,end=" ")
            j=j+2
m=int(input())
for i in range(m):
    n=int(input())
    findJumpingNumbers(n)
