import re
S="The quick brown fox jump over the lazy dog"
word=input("Enter the findind word")
word1=word.lower()
x=re.search(word1,S)
if x:
    a=x.start()
    b=x.end()
    print("%d to %d"%(a,b))
else:
    print("Not found")
