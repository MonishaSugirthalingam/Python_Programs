#Python program to fing the given string is PAN number or not
PAN_No=input("Enter a PAN number")
if len(PAN_No)==10:
    if (PAN_No[0:5].isalpha()) and (PAN_No[0:5].isupper()) and (PAN_No[5:9].isdigit()) and (PAN_No[9].isalpha() and PAN_No[9].isupper()):
        print("Valid")
    else:
        print("Invalid")
else:
    print("invalid" )
