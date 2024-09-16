import Speaker as sp

while True:
    email = input("Enter Your Email : ")


    k, j, d = 0, 0, 0
    if len(email) >= 11:
        if email[0].isalpha():
            if '@' in email and email.count('@') == 1:
                if email[-4] == ".":
                    for i in email:
                        if i == i.isspace():
                            k = 1
                        elif i.isalpha():
                            if i == i.upper():
                                j = 1
                        elif i.isdigit():
                            continue
                        elif i == "_" or i == "." or i == "@":
                            continue
                        else:
                            d = 1
                    if k == 1 or j == 1 or d == 1:
                     
                        sp.randomError()
                    else:
                        sp.rightEmail()
                else:
                    sp.dotCheck()
            else:
                sp.checkAtTheRat()

        else:
            sp.firstLetter()
    else:
        sp.shortLength()
