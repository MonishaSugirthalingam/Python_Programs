Dict={"Mango flavour":15,"Strawberry flavour":30,"Venilla flavour":25,"Choco flavour":35,"Milk flavour":70}
print(Dict)
choose_flavour1=input("Enter your choice")
choose_flavour2=input("Enter your choice")
price1=Dict.get(choose_flavour1)
price2=Dict.get(choose_flavour2)
m=price1+price2
print(m)
print("Sunny and Johnny together have",m,"dollars")
