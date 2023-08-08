"""
AIM  : Apython program to display numbers.the given number is between 0 to 10 then print .else print the adjesent side of the number
Input  Output
1.1
  10     0 1 2 3 4 5 6 7 8 9 10
2. 1
   20    0 1 2 3 4 5 6 7 8 9 10 12
"""

def jumpingNumbers(n):
    count=0
    if(n<=10):
        while count<=n:
            print(count,end=" ")
            count=count+1
        print()
    else:
        a=2
        b=9
        left=11
        while count<=10:
            print(count,end=" ")
            count=count+1
        count=count-1    
        while True:
            if  left%2==1 and count+2<n:
                count=count+a
                print(count,end=" ")
                
            elif left%2==0 and count+9<n:
                count=count+b
                print(count,end=" ")
            else:
                break
            left=left+1
        print()
t=int(input())
for i in range(t):
    jumpingNumbers(int(input()))
