"""
INPUT :          OUTPUT:
2
3 3               4 -1 3
4 -1 3            2 2 -2
2 2 -2            1 3 1
1 3 1
3 5
3 4             1 2 3 4 6
1 2 3 4
5 6 7 8         7 8 9 1 2 3
9 1 2 3
2 6
"""

def greatmat(m,n,mat):
    result=[]
    count=0
    for i in range(int(row)):
        for j in range(int(col)):
            result.append(mat[i][j])
    for i in range(m):
        for j in range(n):
            print(result[count],end=" ")
            count=count+1
        print()
    result.clear()
n=int(input())
for i in range(n):
    mat=[]
    row,col=input().split()
    for i in range(int(row)):
        colv=input().split()
        mat.append(colv)
    m,n=input().split()
    if int(row)*int(col)==int(m)*int(n):
        greatmat(int(m),int(n),mat)
        mat.clear()
    else:
        for i in range(int(row)):
            for j in range(int(col)):
                print(mat[i][j],end=" ")
            print()
        mat.clear()
            
    
