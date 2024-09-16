print('''
1. Admin Mode
2. User Mode
''')
choice = int(input("Enter the choice : "))

user_info = {}
quest = []
ques_data = {}
if choice == 1:
    name = input("Enter the name : ")
    password = input("Enter the pasword : ")

    if name == "" and password == "":
        choice2 = int(input('''
1. Add quetions
2. Update questions
3. Delete questions
4. Add user
'''))

        if choice2 == 1:

            while(1):

                question = input("Enter question : ")
                answer = [input("Enter Answers :") for _ in range(4)]
                ques_data[question] = answer
                with open("QuizData.json", "w") as f:
                    f.write(str(ques_data))
                choice_question = input(
                    "Do u wanna add more questions y or n ? ").lower()
                if choice_question == "n":
                    break
                else:
                    continue

        elif choice2 == 2:
            with open("QuizData.txt", "r") as f:
                x = f.read()
            ques_data1 = dict(x)
            print(type(x))

            # for key, value in ques_data.items():
            #     print(enumerate(key, value))
            question_index = int(input("Enter questions index : "))

        elif choice2 == 3:
            question_index = int(input("Enter questions index : "))

        elif choice2 == 4:
            user_name = input("Enter user name : ")
            user_pass = input("Enter user pass : ")
            user_info[user_name] = user_pass
        else:
            print("Invalid choice")
    else:
        print("Invalid name or password")

elif choice == 2:
    pass
else:
    print("No choice")


# print(ques_data)
