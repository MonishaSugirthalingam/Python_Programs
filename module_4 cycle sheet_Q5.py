"""
AIM: construct a python program to read the three  subject’s marks  secured  by n students during FAT examination.
If a student  secured less than  50 in any subject, the student is failed in that subject.
Count the number of students who failed in each subject and the total number of students who failed in at least one subject.

Example:
Input: S1 = {'m1': 50, 'm2': 40, 'm3':75}
S2 = {'m2': 49, 'm3': 35, 'm4':54}
S3 = {'m1': 77, 'm2': 84, 'm4':51}
Output:
{'m1': 0, 'm2': 2, 'm3': 1, 'm4': 0} 2
"""
s={}
A=int(input("Enter a number of student"))
i=1
for i in range(A):
    h="s"+str(i)
    h={}
    B=int(input("Enter a number of subjects"))
    for j in range(B):
        d1=input("Enter a name of subjects")
        d2=int(input("Enter a mark"))
        h[d1]=d2
        i=i+1
        j=0
        k=1
        if d2<50 and (d1 not in s.keys()):
            s[d1]=k
        elif d2<50 and  s[d1]>=1 :
            count=k+1
            s[d1]=count
        elif d2<50 and (d1 in s.keys()) and s[d1]==0:
            s[d1]=k
        elif d2>50 and (d1 not in s.keys()):
             s[d1]=j
        else:
            pass
print(s)
count=0
k=list(s.values())
for i in k:
    if i>0:
        count=count+1
print(count)        
