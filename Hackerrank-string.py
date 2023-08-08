def merge_the_tools(string, k):
    box=[]
    start=0 
    end=k
    for i in range(k):
        box.append(string[start:end])
        start=end 
        end=end+k 
    r=[]
    for i in box:
        for j in i:
            if j not in r:
                r.append(j)
        print("".join(r))
        r.clear()
               

merge_the_tools("AAABBBCCC",3)
    
