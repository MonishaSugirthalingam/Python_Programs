"""
AIM   : a python code to search the substring s2 and print the position of substring in main String s1, if found. Otherwise print “NotAvailable”.
AUTHOR: MONISHA.S
DATE  : 27-12-2021
"""
s1=input() #read the string
s2=input() #read the substring
n=int(input()) #read the search position
if s2 not in s1: # to search substring in string
    print("NotAvailable") #if it is not available display "Not Available"
else:      #else to find the substring is available in after or before the search position in string
    if s2 in s1[n:]: #if it is after the search position to find theFound position
        s1=list(s1)
        while n>0:
            del s1[n] #remove the elements before the search position
            n=n-1
        print(s1.index(s2[0])) #display the found position
    else: #else if it is before the search position find the found position
        s1=list(s1)
        del s1[n+1:] #remove the elements after the search position
        s1=s1[::-1]
        i="-"+str(s1.index(s2[0]))
        print(int(i)) #display the found position
    
