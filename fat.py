dict1={}
dict2={}
z=[]
key=int(input())
word=input()
count=1
for i in range(97,123):
    letter=chr(i)
    dict1[count]=letter
    dict2[letter]=count
    count=count+1
word1=list(word)
for i in word1:
    s=dict2.get(i)
    x=s+key
    y=dict1.get(x)
    z.append(y)
print(z)
