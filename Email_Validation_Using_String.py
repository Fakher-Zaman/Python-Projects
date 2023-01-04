# a-z
# 0-9
# . _ at a 1 time
# @ at a 1 time
# . at 2, 3 index
email = input("Enter Your Email Here: ")   # g@g.in
k, j, d = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ('@' in email) and (email.count('@') == 1):
            if (email[-4] == '.') ^ (email[-3] == '.'):   # XOR ^
                for i in email:
                    if i == i.isspace():   # State 5
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():   # State 5
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == '_' or i == '.' or i == '@':
                        continue
                    else:   # State 5
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email at state 5")
                else:
                    print("Yup, Email is Valid!")
            else:
                print("Invalid email at state 4")
        else:
            print("Invalid email at state 3")
    else:
        print("Invalid Email at state 2")
else:
    print("Invalid Email at state 1")