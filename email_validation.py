#Email validation using string functions

# closest condition---g@g.in
email = input("Enter Your Email: ")
k = 0
j = 0
d = 0
if len(email) >= 6:  # 1
    if email[0].isalpha():  # 2
        if "@" in email and (email.count('@') == 1):  # 3
            if (email[-3] == ".") ^ (email[-4] == "."):  # 4
                for ch in email:
                    if ch.isspace():  # 5
                        k = 1
                    elif ch.isalpha():
                        if not ch.upper():  # 5
                            j = 1
                    elif ch.isdigit():
                        continue
                    elif ch == "_" or ch == "." or ch == "@":  # 5
                        continue
                    else:
                        d = 1
                # print(k,j,d)
                if k == 1 or j == 1 or d == 1:
                    print("Invalid email 5")
                else:
                    print("Valid Email")

            else:
                print("Invalid Email 4")
        else:
            print("Invalid Email 3")
    else:
        print("Invalid Email 2")

else:
    print("Invalid Email 1")
