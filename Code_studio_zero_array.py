"""
Input:
2  //no.of test case
2 3  //no.of row and column
7 19 3 //first matrix
4 21 0
3 3 \\no.of row and col
1 2 3 // second matrix
4 0 6
7 8 9

Output:
7 19 0
0 0 0
1 0 3
0 0 0
7 0 9

"""
final=[]  
def resultfun(final,case):
    for k in final:
        for i in k:
            for j in i:
                print(j,end=" ")
            print()
def zero(i,j,arr,m,n):
    for row in range(m):
        for col in range(n):
            if row==i or  col==j:
                arr[row][col]=0
    return arr    
def findingzero(arr,m,n):
    result=[]
    flag=0
    for i in range(m):
        for j in range(n):
            if arr[i][j]==0 and flag==0:
                result=result+zero(i,j,arr,m,n)
                flag=1
    return result
case=int(input())
for i in range(case):
    arr=[]
    m,n=input().split()
    for i in range(int(m)):
        a=list(map(int,input().split()))
        arr.append(a)
    final.append(findingzero(arr,int(m),int(n)))
    arr.clear()
resultfun(final,case)

        

        
