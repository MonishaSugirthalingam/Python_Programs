"""
AIM    : A python program to generate a quiz using two files, named Questions.txt and Answers.txt.
AUTHOR : MONISHA.S
DATE   : 26-12-2021
"""
fa=open("Answers.txt","r")
ans=fa.readlines()
fa.close()
points=0
for i in range(2):
    answer=input()
    if answer in ans[i]:
        points=points+50
print(points)
    
