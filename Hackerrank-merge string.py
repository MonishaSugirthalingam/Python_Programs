def merge_string(string,k):
    substring=[]
    start=0
    end=k
    for i in range(len(string)//3):
       substring.append(string[start:end])
       start=end
       end=end+end
    return substring
substring=merge_string(input(),int(input()))
result=[]
for i in substring:
    for j in i:
        if j not in result:
            result.append(j)
    print("".join(result))
    result.clear()
