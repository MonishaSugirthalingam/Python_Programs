import pandas as pd 
#To read the entier file
df=pd.read_csv("supermarket_sales.csv")
#To remove the column as Invoice ID
df.drop("Invoice ID",inplace=True,axis=1)
#To fill the missing values by mode method  in "Gender" column
mode=df["Gender"].mode()
df["Gender"].fillna(mode,inplace=True)
#To remove the other missing values 
df.dropna(inplace=True)
#To calculate and display the total amount city wise
Yangon_amount=Naypyitaw_amount=Mandalay_amount=0
for x in df.index:
    if df.loc[x,"City"]=="Yangon":
        Yangon_amount=Yangon_amount+df.loc[x,"Total"]
    if df.loc[x,"City"]=="Naypyitaw":
        Naypyitaw_amount=Naypyitaw_amount+df.loc[x,"Total"]
    if df.loc[x,"City"]=="Mandalay":
        Mandalay_amount=Mandalay_amount+df.loc[x,"Total"]
print("City Yagon's total sales amount") 
print(Yangon_amount)
print("City Naypyitaw's total sales amount")
print(Naypyitaw_amount)
print("City Mandalay's total sales amount")
print(Mandalay_amount)
#To calculate and display the total  amount using Ewallet Branch wise
Ewallet_Branch=0
for y in df.index:
    if df.loc[y,"Payment"]=="Ewallet":
        Ewallet_Branch=Ewallet_Branch+df.loc[y,"Total"]
print("total amount from Ewallet Branch")
print(Ewallet_Branch)
#To compute the  number of Males and Females customers and display the how many of them are members
Male_member=Female_member=0
for z in df.index:
    if df.loc[z,"Gender"]=="Male" and df.loc[z,"Customer type"]=="Member":
        Male_member= Male_member+1
    if df.loc[z,"Gender"]=="Female" and df.loc[z,"Customer type"]=="Member":
        Female_member= Female_member+1 
print("the number of Male members")
print(Male_member)
print("the number of Female member")
print(Female_member)
#To Display the quantity of each type of products purchased by either Male/Female customers
Electronic_accessories=Fashion_accessories=Food_and_beverages=Health_and_beauty=Home_and_lifestyle=Sports_and_travel=0
pro1_tol_cast= pro2_tol_cast= pro3_tol_cast= pro4_tol_cast= pro5_tol_cast= pro6_tol_cast=0
for a in df.index:
    if df.loc[a,"Product line"]=="Electronic accessories":
        Electronic_accessories=Electronic_accessories+df.loc[a,"Quantity"]
        pro1_tol_cast= pro1_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
    if df.loc[a,"Product line"]=="Fashion accessories":
        Fashion_accessories=Fashion_accessories+df.loc[a,"Quantity"]
        pro2_tol_cast= pro2_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
    if df.loc[a,"Product line"]=="Food and beverages":
        Food_and_beverages=Food_and_beverages+df.loc[a,"Quantity"]
        pro3_tol_cast= pro3_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
    if df.loc[a,"Product line"]=="Health and beauty":
        Health_and_beauty=Health_and_beauty+df.loc[a,"Quantity"]
        pro4_tol_cast= pro4_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
    if df.loc[a,"Product line"]=="Home and lifestyle":
        Home_and_lifestyle=Home_and_lifestyle+df.loc[a,"Quantity"]
        pro5_tol_cast= pro5_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
    if df.loc[a,"Product line"]=="Sports and travel":
        Sports_and_travel=Sports_and_travel+df.loc[a,"Quantity"]
        pro6_tol_cast= pro6_tol_cast+(df.loc[a,"Quantity"]*df.loc[a,"Unit price"])
print("the quatity of Electronic_accessories") 
print(Electronic_accessories)
print("the quatity of Fashion_accessories")
print(Fashion_accessories)
print("the quatity of Food_and_beverages")
print(Food_and_beverages)
print("the quatity of Health_and_beauty") 
print(Health_and_beauty)
print("the quatity of Home_and_lifestyle")
print(Home_and_lifestyle)
print("the quatity of Sports_and_travel")
print(Sports_and_travel)
#To calculate the total tax amount for each type of products 
print("the total tax for  Electronic_accessories") 
tax_Electronic_accessories=pro1_tol_cast*0.05
print(tax_Electronic_accessories)
print("the total tax for Fashion_accessories")
tax_Fashion_accessories=pro2_tol_cast*0.05
print(tax_Fashion_accessories)
print("the total tax for Food_and_beverages")
tax_Food_and_beverages=pro3_tol_cast*0.05
print(tax_Food_and_beverages)
print("the total tax for Health_and_beauty") 
tax_Health_and_beauty=pro4_tol_cast*0.05
print(tax_Health_and_beauty)
print("the total tax for Home_and_lifestyle")
tax_Home_and_lifestyle=pro5_tol_cast*0.05
print(tax_Home_and_lifestyle)
print("the total tax for Sports_and_travel")
tax_Sports_and_travel=pro6_tol_cast*0.05
print(tax_Sports_and_travel)
#To create a new column 
df["Date"]=pd.to_datetime(df["Date"])
df["Date"]=pd.to_datetime(df["Date"]).dt.strftime('%d-%m-%Y')
New_date=pd.Series(df["Date"])
for i in New_date:
    df["New_date"]=i
    df.to_csv("supermarket_sales.csv",index=False)

df["month"]=pd.DatetimeIndex(df["New_date"]).month
for b in df.index:
    if df[]
        
