def decodeString(s):

    # Write your code here.
    st=[]
    e=[]
    new=""
    for i in s:
        if (i.isdigit() or i=="[" or i=="]"):
            st.append(i)
        if (i.isalpha()):
            e.append(i)
    for j in st[::-1]:
        if(j.isdigit()):
                num=int(j)
                letter=e.pop()
                new=new+letter
                new=new[::-1]
                new=new*num
                st.pop()
        else:
                st.pop()
    print(new)
decodeString("3[a2[b]]")    
        
        
