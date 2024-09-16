
import random as r
from time import *
import pandas as pd
from prettytable import PrettyTable
x = PrettyTable(padding_width=5)


def mistake(partest, usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i] != usertest[i]:
                error += 1
        except:
            error += 1
    return error


def speed_time(time_s, time_e, userinput):
    time_delay = round((time_e - time_s), 2)
    speed = round(len(userinput)/time_delay)

    return round(speed)


x.field_names = ["Welcome To Typing Speed Checker"]
x.add_row(["1. Admin"])
x.add_row(["2. User"])
print(x)

choice = input("Choose: ")
print()
if choice == "1":
    userAdmin = input("Enter Name : ")
    userPass = input("Enter Pass : ")

    with open("F:\\Python\\Project\\20 Projects\\TypingSpeed\\user.txt", "r") as user:
        x = user.read().split()

    ask = True
    list1 = []
    if userAdmin == x[0] and userPass == x[1]:
        print("Successfully Login..!\n")
        while ask:
            paragraphText = input("Enter The Paragraph : \n")
            list1.append(paragraphText)
            with open('para.txt', 'w') as f:
                f.write(str(list1))

            askmore = input("Do You wanna Add more paragraph y or n ?").lower()
            if "n" in askmore:
                ask = False
            else:
                continue
    else:
        print("Inncorrect Name or Password")

    df = pd.DataFrame(list1, columns=["Paragraphs"])
    print(df)

elif choice == "2":
    with open('para.txt', 'r') as f:
        h = f.read()
        t = h.split()
        # print(type(t))
        # print(t)

    userName = input("Enter Name: ")
    print(f'------Welcome {userName} In Typing speed-------')

    r.shuffle(t)
    textChoice = "abcd"

    print(textChoice)
    print()
    time1 = time()
    testinput = input("Enter Your Text: \n")
    time2 = time()

    print(f"Your Speed = {speed_time(time1,time2,testinput)} w/s")
    print(f"Your Error's = {mistake(textChoice,testinput)}")

else:
    print("Error")
