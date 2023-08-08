List=[10,20,30,40,50,60,70,80,90,100]
k=int(input("Enter a value of k"))
s=[]
# number of looping
for i in List:
    # subtract the specific number which equal to k
    for n in List:
        g=n-i
        #if the number of pairs whose difference equal to k 
        if g==k:
            h=(i,n)
            #convert into list type
            L=list(h)
            #and store it empty list as s
            s.append(L)
# lenth of list             
N=len(s)
#print the number of pairs 
print("Number of pairs",N)
      
