"""
1. Push(num): Push the given number in the stack.
2. Pop: Remove and return the top element from the stack if present, else return -1.
3. Top: return the top element of the stack if present, else return -1.
4. getMin: Returns minimum element of the stack if present, else return -1.
Ex:Input
1 \\no.of test case
5  \\ no.of operation
1 1
1 2
4
2
3
Explanation:
For the first two operations, we will just insert 1 and then 2 into the stack which was empty earlier. So now the stack is => [2,1]
In the third operation, we need to return the minimum element of the stack, i.e., 1. So now the stack is => [2,1]
For the fourth operation, we need to pop the topmost element of the stack, i.e., 2. Now the stack is => [1]
In the fifth operation, we return the top element of the stack, i.e. 1 as it has one element. Now the stack is => [1]

So, the final output will be: 
1 2 1   \\output
"""
a=[]
b=[]
fin=[]
re=[]
def operating(a,b,re):
    for i in a:
        if i=="2" and len(b)!=0:
            pop=b.pop()
            re.append(pop)
        if i=="3" and len(b)!=0:
            re.append(b[0])
        if i=="4" and len(b)!=0:
            re.append(min(b))
        if (i=="2" or i=="3" or i=="4") and len(b)==0:
            re.append("-1")
    return re
n=int(input())
for i in range(n):
    operation=int(input())
    for j in range(operation):
        s=input()
        if len(s)==1:
            a.append(s)
        else:
            opera,inputs=s.split()
            b.append(inputs)
re.clear()
print(a,b)
fin.append(operating(a,b,re))
a.clear()
b.clear()
for i in fin:
    x=list(map(int,i))
    for j in x:
        print(j,end=" ")
    print()


