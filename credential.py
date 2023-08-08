dict1={}
uni_user=[]
passbox=[]
while True:
    user=input()
    if user=="dict_login_credentials":
        print(dict1)
        break
   
    if user in uni_user:
        print("TO take another user name")
        user=input()
        uni_user.append(user)
    else:
        uni_user.append(user)
   
    password=input()
    passbox.append(password)
    dict1[user]=password
    
    
