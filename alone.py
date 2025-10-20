import random
from random_word import RandomWords
r = RandomWords()
from checker import *
INPUT_FILE = "./common_passwords.txt"
OUTPUT_FILE = "./checking_password_log.txt"

def length_checker():
    length = len(username)
    if length < 10:
        print("you need 10 chars or more")
    else:
        print("Your username is a good length")

def check_first_char(username):
    print(username[0])
    if username.isalpha():
        print("accepted first char")

def generate_username():
    first=input("First name: ")
    last=input ("Last name: ")
    username = (f"{first[0]}-{random.randint(1,99)}-{last}-{r.get_random_word()}")
    return username

def check_no_underscores(username):
    underscore = False
    for i in username:
        if i == "_":
            underscore = True

    if underscore:
        print("There is an underscore")
    else:
        print("no underscore")



def menu(option):
    print(option)
    match option:
        case 1:
            print("---Generate username---")
            print(generate_username())
        case 2:
            username = input("What is your username")
            length_checker(username)
        case 3:
            username = input("What is your username")
            check_first_char(username)
        case 4:
            username = input("What is your username: ")
            check_no_underscores(username)
        case 5:
            password= input("What is you password?: ")
            is_common_password(password)

        case _:
            print("no")


while True:
    try:
        print("----\nuser name menu system\noptions=\n1-generate username\n2-length check:\n 3-First character checker: ")
        option=int(input("input option(1:3): "))
        menu(option)
        break
    except:
        print("input a valid number")