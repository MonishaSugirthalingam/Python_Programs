"""
INPUT:
BANANA
OUTPUT:
Stuart 12  \\ names are given by the question
"""
s=input()
vowel=[]
result=[]
dict1={}
for i in range(len(s)):
    if s[i]=="A":
        vowel.append(i)
    if s[i]=="E":
        vowel.append(i)
    if s[i]=="I":
        vowel.append(i)
    if s[i]=="O":
        vowel.append(i)
    if s[i]=="U":
        vowel.append(i)
consonent=[]
for i in range(len(s)):
    if s[i]!="A" and s[i]!="E" and s[i]!="I" and s[i]!="O" and s[i]!="U":
        consonent.append(i)
def pointsforKevin(vowel):
    kavinpoints=0
    for i in range(len(vowel)):
        for i in range(vowel[i],len(s)):
            kavinpoints=kavinpoints+1
    return kavinpoints
person1=pointsforKevin(vowel)
dict1[person1]="Kavin"
result.append(person1)
def pointsforStuart(consonent):
    stuartpoints=0
    for i in range(len(consonent)):
        for i in range(consonent[i],len(s)):
            stuartpoints=stuartpoints+1
    return stuartpoints
person2=pointsforStuart(consonent)
result.append(person2)
dict1[person2]="Stuart"
winner=max(result)
print(dict1.get(winner),winner)


        
        
