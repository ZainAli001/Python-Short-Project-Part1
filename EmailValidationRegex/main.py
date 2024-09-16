import re


email_validation= "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
userInput= input("Enter Your email :")
if re.search(email_validation,userInput):
    print("Correct Email")
else:
    print("Wrong Email")