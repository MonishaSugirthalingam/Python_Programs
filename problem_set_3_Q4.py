f=open("write.txt","w")
f.write("positive_____hello all how are you_____moni"+"\n")
f.write("negative_____i am so bad_____hari@delhi"+"\n")
f.write("nutral_____yeah_not_bad_____thanu@chennai"+"\n")
f.write("positive_____yeah i am very good_____sabu@chinne"+"\n")
f.write("negative_____how your fine_____monstor@sky"+"\n")
f.write("positive_____hey food is ready for all_____mom@srilanga"+"\n")
f.write("nutral_____hhhhh!!!!!1_____nuuu@yahoo"+"\n")
f.write("negative_____food is very bad_____somo@eroo"+"\n")
f.write("positive_____super!!!_____moni"+"\n")
f.close()
f=open("write.txt","r")
List=f.readlines()
f.close()
s=[]
name=[]
text1=[]
text2=[]
text3=[]
for i in List:
    d=i.split("_____")
    text1.append(d[0])
    text2.append(d[1])
    text3.append(d[2])
    d.clear()

count=len(List)
print(count)
f1=open("sentiment.txt","w")
for i in text1:
    i=i+"\n"
    f1.write(i)
f1.close()
f2=open("twttext.txt.txt","w")
for i in text2:
    i=i+"\n"
    f2.write(i)
f2.close()
f3=open("user.txt","w")
for i in text3:
    i=i+"\n"
    f3.write(i)
f3.close()
for i in List:
    s.append(i.split("_____"))
for i in List:
    d=i.split("_____")
    name.append(d[2])
for i in name:
    if name.count(i)>1:
        name.remove(i)
users=len(name)
print(users)
count1=0
for i in s:
    for j in i:
        if j=="positive":
            count1=count1+1
print(count1)
count2=0
for i in s:
    for j in i:
        if j=="negative":
            count2=count2+1       
print(count2)
count3=0
for i in s:
    for j in i:
        if j=="nutral":
            count3=count3+1
print(count3)
sentiment_score=(count1*1)+(count2*-1)+(count3*0)
print(sentiment_score)

         
