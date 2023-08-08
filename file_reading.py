fq=open("Questions.txt","w")
fq.write("1. Who is the prime minister of India? \n")
fq.write("A. Narendra Modi B. Shivraj Patil\n") 
fq.write("2. Who is the President of USA?\n") 
fq.write("A. Donald Trump B. Joe Biden \n")
fq.close()
fa=open("Answers.txt","w")
fa.write("1.A\n")
fa.write("2.B\n") 
fa.close()
fa=open("Answers.txt","r")
ans=fa.readlines()
fa.close()
fq=open("Questions.txt","r")
s=fq.readlines()
fq.close()
points=0
print(ans)
for i in range(2):
    answer=input()
    if answer in ans[i]:
        points=points+50
    fq.close()
print(points)

    
