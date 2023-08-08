def count_substring(string, sub_string):
    result=[]
    count=0
    for i in range(len(string)):
        if string[i]==sub_string[0]:
            result.append(string[i:i+len(sub_string)])
    for i in result:
        if sub_string in i:
            count=count+1
    return count
print(count_substring("ABCDCDC","CDC"))
