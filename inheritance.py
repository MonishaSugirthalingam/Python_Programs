class SchoolOffice :
    def display(key,school,a,b,c):
        print(school," Details are Update....!")
        print("             For Reference ",a,"\t",b,"\t",c)
        print("Thank You!!!!")
        
class SCOPE(SchoolOffice):
    def Details1(key):
        print("From SCOPE School")
        print("Enter the Number of Students :",end=" ")
        num=int(input())
        print("Enter the Number of Pass Students :",end=" ")
        passes=int(input())
        print("Enter the Number of Fail Students :",end=" ")
        fails=int(input())
        key.display("SCOPE",num,passes,fails)
        print("---------------------------------------------------------------")

class SENCE(SchoolOffice):
    def Details2(key):
        print("From SENCE School")
        print("Enter the Number of Students :",end=" ")
        num=int(input())
        print("Enter the Number of Pass Students :",end=" ")
        passes=int(input())
        print("Enter the Number of Fail Students :",end=" ")
        fails=int(input())
        key.display("SENCE",num,passes,fails)
        print("---------------------------------------------------------------")
        
class SITE(SchoolOffice):
    def Details3(key):
        print("From SITE School")
        print("Enter the Number of Students :",end=" ")
        num=int(input())
        print("Enter the Number of Pass Students :",end=" ")
        passes=int(input())
        print("Enter the Number of Fail Students :",end=" ")
        fails=int(input())
        key.display("SITE",num,passes,fails)
        print("---------------------------------------------------------------")

class IT(SITE):
    def call(key):
        key.Details3()

class CSE(SCOPE):
    def call(key):
        key.Details1()

class ECE(SENCE):
    def call(key):
        key.Details2()
    
        
#Creating a Object for class IT  
obj1=IT()
obj1.call()
#Creating a Object for Class ECE
obj2=ECE()
obj2.call()
#Creating aObject for Class CSE
obj3=CSE()
obj3.call()
    
