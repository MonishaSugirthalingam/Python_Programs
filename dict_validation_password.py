users={"kani":"kani123@y","shalini":"shank@han","Banu":"see123@45","priya":"ramu09#","Jamun":"jams@134#"}
fromuser_username=input("Enter your username :")
fromuser_passward=input("Enter your password :")
fromdict_username=list(users.keys())
fromdict_password=list(users.values())
if (fromuser_username in fromdict_username) and (fromuser_passward in fromdict_password):
    print("User is Valid")
else:
    print("User is Notvalid")
