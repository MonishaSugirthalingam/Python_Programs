"""
Input:
4
1 3 5 6
4
1 3 8 9
Output;
5
6
8
9
""""


n=int(input())
set1=set(map(int,input().split()))
n1=int(input())
set2=set(map(int,input().split()))
s=set1|set2
s1=set1&set2
box=list(s-s1)
box.sort()
for i in box:
    print(i)
