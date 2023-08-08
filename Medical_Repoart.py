No_of_patients=int(input("How many numbers of patients needs medical report :"))
Types_of_Test={"BT":"Heamoglobin","UT":"Amonia level","BP":"Blood pressure","DT":"Sugar level","BMI":"Adul BMI calculater"}
print("Types of Test")
print(Types_of_Test)
Name1=[]
rec={}
for i in range(No_of_patients):
    Name=input("please enter your name")
    Name1.append(Name)
    Test=int(input("How many test we want to go?"))
    for i in range(Test):
        Testname=input(" please Enter the name of the test")
        value=int(input("Enter the value"))
        if Testname=="BMI":
            if value>=20 and value<=30:
                rec["BMI-TEST"]="NORMAL"
            else:
                rec["BMI-TEST"]="ABNORMAL"
        if Testname=="UT":
            if value>=35.5 and value<=40:
                rec["UT-TEST"]="NORMAL"
            else:
                rec["UT-TEST"]="ABNORMAL"
        if Testname=="BT":
            if value>=12 and value<=15:
                rec["BT-TEST"]="NORMAL"
            else:
                rec["BT-TEST"]="ABNORMAL"
        if Testname=="BP":
            if value>=120 and value<=150:
                rec["BP-TEST"]="NORMAL"
            else:
                rec["BP-TEST"]="ABNORMAL"
        
        if Testname=="DT":
            if value>=20 and value<=30:
                rec["DT-TEST"]="NORMAL"
            else:
                rec["DT-TEST"]="ABNORMAL"
                
f=set(rec.items())
d=dict.fromkeys(Name1,f)
patient_report=input("REPORT : Please Enter the name of the patient")
Report=d.get(patient_report)
print("MR/MISS/MRES  ",patient_report,"Health report")
print(Report)
        
