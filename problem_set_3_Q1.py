import re
Email_ID=input()
formats=re.compile(r"^([a-zA-Z0-9]+[\._])*[a-zA-Z0-9]+[@][a-zA-Z0-9-]?([((gmail)|(yahoo)|(Hotmail)|(rediffmail)|(vitstudent)|\w+]{3,})([\.]
                   [(gov)(com)(org)(net)(edu.in|edu.fr|edu.au|edu)(ac.in|ac.fr|ac.au|ac)])$")
validation=re.search(formats,Email_ID)
if validation:
    print("Valid")
else:
    print("Invalid")
