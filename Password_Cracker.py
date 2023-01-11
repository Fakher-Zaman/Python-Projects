# $ pip install random2
from random import *

user_pass = input("Enter your password: ")

password = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
                     'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G',
                     'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z', '@', '#', '$', '%', '=', ':', '?',
                     '*', '(', ')', '<', '/', '|', '~', '>', '.', 'H'] 
LOCASE_CHARACTERS = []
 
UPCASE_CHARACTERS = []
 
SYMBOLS = []
 
guess = ""

while(guess != user_pass):
    guess = ""
    for letter in range(len(user_pass)):
        guess_letter = password[randint(0, 25)]
        guess = str(guess_letter) + str(guess)
        print(guess)

print("Your password is", guess)