"""
Input:
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Output:
4 //sum of left elements
"""
n = int(input())
sums=0
st = set(map(int, input().split()))
loop=int(input())
for i in range(loop):
    try:
        s,num=input().split()
        if s=="remove":
            st.remove(int(num))
        if s=="discard":
            st.discard(int(num))
        if s=="pop":
            if int(num) in st:
                st.pop(int(num))
    except:
        st.pop()
for i in st:
    sums=sums+i
print(sums)

        
