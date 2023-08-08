"""
Input:
aabcdeffgabcdef
abcdef
Output:
(1,6)
(9,14)
"""
string="aabcdeffgabcdef"
substring="abcdef"
end=len(substring)
empty=[]
result=[]
for i in range(len(string)):
    b=string[i:end]
    if b==substring:
       empty.append(i)
       empty.append(end-1)
       s=empty
       result.append(tuple(s))
    end=end+1
    empty.clear()
for i in result:
    print(i)
