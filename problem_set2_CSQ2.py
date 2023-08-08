
import datetime
ASE=0
SE=0
TL=0
PM=0
RE=0
n=int(input("Enter a number of employees"))
for i in range(n):
    Date_of_joining=input()
    Current_date="2021-11-30"
    start=datetime.date(int(Date_of_joining[0:4]),int(Date_of_joining[5:7]),int(Date_of_joining[8:]))
    end=datetime.date(int(Current_date[0:4]),int(Current_date[5:7]),int(Current_date[8:]))
    days=end-start
    days=str(days)
    day=days.split()
    year=(int(day[0])//365)
    if year<2:
        SE=SE+1
    if year>=2 and year<7:
        ASE=ASE+1
    if year>=8 and year<=19:
        TL=TL+1
    if year>20 and year<32:
        PM=PM+1
    if year>=32:
        RE=RE+1
print(ASE,"Probationers are workung as Associate Software Engineers")
print(SE,"Permanent Employee is working as Software Engineer")
print(TL,"Senior Employees are working as Team Leaders")
print(PM,"Executive Employee is working as Project Manager")
print(RE,"Employee is Retried")
