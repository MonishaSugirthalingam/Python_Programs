"""
Input:
16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Output:
38
"""

n1=int(input())
sums=0
s1=set(map(int,input().split()))
loop=int(input())
for i in range(loop):
    name,time=input().split()
    if name=="intersection_update":
        ele=set(map(int,input().split()))
        s1.intersection_update(ele)
    if name=="update":
        ele=set(map(int,input().split()))
        s1.update(ele)
    if name=="symmetric_difference_update":
        ele=set(map(int,input().split()))
        s1.symmetric_difference_update(ele)
    if name=="difference_update":
        ele=set(map(int,input().split()))
        s1.difference_update(ele)
for i in s1:
    sums=sums+i
print(sums)
