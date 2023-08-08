import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
#To read the entier file
df=pd.read_csv("supermarket_sales.csv")
#To remove the column as Invoice ID
df.drop("Invoice ID",inplace=True,axis=1)
#To fill the missing values by mode method  in "Gender" column
df=df.dropna(axis=0,how='any',subset=['Gender'])
mode=df["Gender"].mode()
df["Gender"].fillna(mode,inplace=True)
#To calculate and display the total amount city wise
Yangon_amount=Naypyitaw_amount=Mandalay_amount=0
for x in df.index:
    if df.loc[x,"City"]=="Yangon":
        Yangon_amount=Yangon_amount+df.loc[x,"Total"]
    if df.loc[x,"City"]=="Naypyitaw":
        Naypyitaw_amount=Naypyitaw_amount+df.loc[x,"Total"]
    if df.loc[x,"City"]=="Mandalay":
        Mandalay_amount=Mandalay_amount+df.loc[x,"Total"]
tol_amo_city_wise={"City":["Yangon","Naypyitaw","Mandalay"],"Total amount city wise":[Yangon_amount,Naypyitaw_amount,Mandalay_amount]}
print("The toyal sales amount city wise")
print(pd.DataFrame(tol_amo_city_wise))
print("-"*20)
#To calculate and display the total  amount using Ewallet Branch wise
Ewallet_Branch = df.loc[df.Payment == "Ewallet", ["Branch", "Payment", "Total"]]
print("total amount from Ewallet in Branch wise")
print(Ewallet_Branch.groupby(["Branch"]).sum())
print("-"*20)
#To compute the  number of Males and Females customers and display the how many of them are members
Male_member=Female_member=0
for z in df.index:
    if df.loc[z,"Gender"]=="Male" and df.loc[z,"Customer type"]=="Member":
        Male_member= Male_member+1
    if df.loc[z,"Gender"]=="Female" and df.loc[z,"Customer type"]=="Member":
        Female_member= Female_member+1 
members={"Sex":["Male","Female"],"Number of members":[Male_member,Female_member]}
print("Number of Male and Female customers")
print(pd.DataFrame(members))
print("-"*20)
#To Display the quantity of each type of products purchased by either Male/Female customers
Electronic_accessories=Fashion_accessories=Food_and_beverages=Health_and_beauty=Home_and_lifestyle=Sports_and_travel=0
for a in df.index:
    if df.loc[a,"Product line"]=="Electronic accessories":
        Electronic_accessories=Electronic_accessories+df.loc[a,"Quantity"]
    if df.loc[a,"Product line"]=="Fashion accessories":
        Fashion_accessories=Fashion_accessories+df.loc[a,"Quantity"]
    if df.loc[a,"Product line"]=="Food and beverages":
        Food_and_beverages=Food_and_beverages+df.loc[a,"Quantity"]
    if df.loc[a,"Product line"]=="Health and beauty":
        Health_and_beauty=Health_and_beauty+df.loc[a,"Quantity"]
    if df.loc[a,"Product line"]=="Home and lifestyle":
        Home_and_lifestyle=Home_and_lifestyle+df.loc[a,"Quantity"]
    if df.loc[a,"Product line"]=="Sports and travel":
        Sports_and_travel=Sports_and_travel+df.loc[a,"Quantity"]
print("The total quanty of each item")
quanty_of_each_item={"Product Name":["Electronic accessories","Fashion accessories","Food and beverages","Health and beauty","Home and lifestyle","Sports and travel"],"Total sale":[Electronic_accessories,Fashion_accessories,Food_and_beverages,Health_and_beauty,Home_and_lifestyle,Sports_and_travel]}
print(pd.DataFrame(quanty_of_each_item))
print("-"*20)
#To calculate the total tax amount for each type of products 
tol_tax_amount = df[["Product line", "Tax 5%"]]
print("the total tax amount for each type of products ")
print(tol_tax_amount.groupby(["Product line"]).sum())
print("-"*20)
df.insert(13,column="New Date",value="")
df["Date"]=pd.to_datetime(df["Date"]).dt.strftime('%d-%m-%Y')
s=pd.DataFrame(df["Date"])
s["Date"]=pd.to_datetime(s["Date"])
s["Date"]=pd.to_datetime(s["Date"]).dt.strftime('%d-%m-%Y')
p=list(s["Date"])
for i in range(0,len(s["Date"]),1):
    df["New Date"][i]=p[i]
print("A new Data column")
print(df["New Date"])
print("-"*20)
df["month"]=pd.DatetimeIndex(df["Date"]).month 
groups=df.groupby("month")
jan=groups.get_group(1)
feb=groups.get_group(2)
mar=groups.get_group(3)
aprl=groups.get_group(4)
may=groups.get_group(5)
jun=groups.get_group(6)
july=groups.get_group(7)
aug=groups.get_group(8)
sep=groups.get_group(9)
octo=groups.get_group(10)
nov=groups.get_group(11)
dec=groups.get_group(12)
price11=price12=price13=price14=price15=price16=0
for i in jan.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price11=price11+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price12=price12+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price13=price13+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price14=price14+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price15=price15+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price16=price16+df.loc[i,"Total"]
price21=price22=price23=price24=price25=price26=0
for i in feb.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price21=price21+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price22=price22+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price23=price23+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        pric24=price24+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price25=price25+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price26=price26+df.loc[i,"Total"]
price31=price32=price33=price34=price35=price36=0
for i in mar.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price31=price31+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price32=price32+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price33=price33+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price134=price14+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price35=price35+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price36=price36+df.loc[i,"Total"]
price41=price42=price43=price44=price45=price46=0
for i in aprl.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price41=price41+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price42=price42+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price43=price43+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price44=price44+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price45=price45+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price46=price46+df.loc[i,"Total"]
price51=price52=price53=price54=price55=price56=0
for i in may.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price51=price51+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price52=price52+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price53=price53+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price54=price54+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price55=price55+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price56=price56+df.loc[i,"Total"]
price61=price62=price63=price64=price65=price66=0
for i in jun.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price61=price61+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price62=price62+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price63=price63+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price64=price64+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price65=price65+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price66=price66+df.loc[i,"Total"]
price71=price72=price73=price74=price75=price76=0
for i in july.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price71=price71+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price72=price72+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price73=price73+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price74=price74+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price75=price75+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price76=price76+df.loc[i,"Total"]
price81=price82=price83=price84=price85=price86=0
for i in aug.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price81=price81+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price82=price82+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price83=price83+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price84=price84+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price85=price85+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price86=price86+df.loc[i,"Total"]
price91=price92=price93=price94=price95=price96=0
for i in sep.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price91=price91+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price92=price92+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price93=price93+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price94=price94+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price95=price95+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price96=price96+df.loc[i,"Total"]
price01=price02=price03=price04=price05=price06=0
for i in octo.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price01=price01+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price02=price02+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price03=price03+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price04=price04+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price05=price05+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price06=price06+df.loc[i,"Total"]
price011=price012=price013=price014=price015=price016=0
for i in nov.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price011=price011+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price012=price012+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price013=price013+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price014=price014+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price015=price015+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price016=price016+df.loc[i,"Total"]
price021=price022=price023=price024=price025=price026=0
for i in dec.index:
    if df.loc[i,"Product line"]=="Electronic accessories":
        price021=price021+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Fashion accessories":
        price022=price022+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Food and beverages":
        price023=price023+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Health and beauty":
        price024=price024+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Home and lifestyle":
        price025=price025+df.loc[i,"Total"]
    if df.loc[i,"Product line"]=="Sports and travel":
        price026=price026+df.loc[i,"Total"]
dataframe={"month":["Jan","Feb","March","Aprl","May","June","July","Aug","Sep","Oct","Nov","Dec"],"Electronic accessories":[price11,price21,price31,price41,price51,price61,price71,price81,price91,price01,price011,price021],"Fashion accessories":[price12,price22,price32,price42,price52,price62,price72,price82,price92,price02,price012,price022],"Food and beverages":[price13,price23,price33,price43,price53,price63,price73,price83,price93,price03,price013,price023],
    "Health and beauty":[price14,price24,price34,price44,price54,price64,price74,price84,price94,price04,price014,price024],"Home and lifestyle":[price15,price25,price35,price45,price55,price65,price75,price85,price95,price05,price015,price025],"Sports and travel":[price16,price26,price36,price46,price56,price66,price76,price86,price96,price06,price016,price026]
}
result=pd.DataFrame(dataframe)
print(result.to_string())
print("-"*50)
count = df.loc[df.Rating < 7.0 , ["Product line", "Rating"]]
print(count.groupby(["Product line"]).count())
print("The count of each type products got less than 7 rating")
print("-"*50)
df["Branch"]=df["Branch"].astype("category").cat.codes
df["City"]=df["City"].astype("category").cat.codes
print("The correlation between Branch and City")
print(df["Branch"].corr(df["City"]))
print("-"*50)



