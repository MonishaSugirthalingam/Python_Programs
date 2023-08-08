k=[]
s=""
Dict={'a':'d','b':'e','c':'f','d':'g','e':'h','f':'i','g':'j',
      'h':'k','i':'l','j':'m','k':'n','l':'o','m':'p','n':'q',
      'o':'r','p':'s','q':'t','r':'u','s':'v','t':'w','u':'x',
      'v':'y','w':'z','x':'a','y':'b','z':'c'}
word=input("Enter a word:")
word1=word.lower()
list1=list(word1)
for i in list1:
    g=Dict.get(i)
    k.append(g)
    j=s.join(k)
print(j)    
           
