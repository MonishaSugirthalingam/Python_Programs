#Email validation
name=input("Enter your name : ")
num=input("Enter any random number : ")
atsimbol=input("Enter simbol @ : ")
org=input("Enter any organisation : ")
dot=input("Enter .in or .com : ")
Email=name+num+atsimbol+org+dot
fromEmail=name+num
import re
if re.findall("(A-Z|a-z)+(a-z|A-Z)+[0-9]+",fromEmail):
    print("Valid")
else:
    print("Invalid")

#Another method
#count1=count2=count3=0
#for i in fromEmail:
    #if i.isupper():
        #count1=1 
    #if i.islower():
        #count2=1 
    #if i.isdigit():
       # count3=1 
#if count1+count2+count3==3:
    #print("Valid")
#else:
    #print("Invalid")
