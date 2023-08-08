password=input()
for i in password:
    if (i.isupper()) and(i.islower()) and (i=='$' or i=='#' or i=='@') and (len((password))>=6 or len((password))<=16):
        print("valide password")
    else:
        print("invalid password")
