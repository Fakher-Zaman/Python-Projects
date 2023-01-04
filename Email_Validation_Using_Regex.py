# Regex = Regular Expression
# a-z
# 0-9
# . _ at a 1 time
# @ at a 1 time
# . at 2, 3 index

import re    # re = regular expression

# ^ symbol for start in regex
# [] for enclosed condition
# + symbol for add condition in regex
# \ symbol for searching in regex
# ? symbol for true/false statement in regex
# \w symbol for reverse search
# $ symbol for reverse
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input("Enter Your Email Here: ")

if re.search(email_condition, user_email):
    print("Yup, Email is Valid!")
else:
    print("Email is Invalid!")