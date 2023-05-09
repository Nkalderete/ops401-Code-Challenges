#!/usr/bin/python3
# Nick Aldereet
# Worked with Geneva and Sierra
# Sources: 
    # https://www.shiksha.com/online-courses/articles/validating-passwords-using-python-regex-match/
    # https://www.geeksforgeeks.org/password-validation-in-python/#     


import time
import re 

def mode1():
    # Ask user for wordlist file path
    filepath = input("Enter the file path of your dictionary:\n")
    
    # Open the file and read each word
    with open(filepath) as file:
        for line in file:
            word = line.strip()
            time.sleep(1)
            print(word)
            
def mode2():
    # Ask user for wordlist file path
    filepath = input("Enter the file path of your dictionary:\n")

    with open(filepath) as file:
        password_list = [line.strip() for line in file]
        
        # Ask user for password and check if it's in the list
        while True:
            password = input("Please enter your password: \n")
            if password in password_list:
                print("Your password is weak. Please beef it up and try again!")
            else:
                print("Your password is beefy enough!")
                break

def mode3():
    # Ask user for password
    password = input("Please enter your password: \n")
        # Check if password meets length requirement
    if len(password) >= 6:
        length_check = True
    else:
        length_check = False
    
    # Check if password has at least 1 capital letter
    if re.search('[A-Z]', password):
        capital_check = True
    else:
        capital_check = False
    
    # Check if password has at least 2 numbers
    if len(re.findall('\d', password)) >= 2:
        number_check = True
    else:
        number_check = False
    
    # Check if password has at least 1 symbol
    if re.search('[^a-zA-Z0-9]', password):
        symbol_check = True
    else:
        symbol_check = False
    
    # Print which password complexity metrics were satisfied
    if length_check and capital_check and number_check and symbol_check:
        print("SUCCESS! Password meets beefy requirements.")
    else:
        print("Beefy password requirements NOT met. The following requirements MUST be met:\n")
        if not length_check:
            print("Please use at least 6 characters\n")
        if not capital_check:
            print("Please use at least 1 capital letter\n")
        if not number_check:
            print("Please use at least 2 numbers\n")
        if not symbol_check:
            print("Please use at least 1 symbol\n")

# User menu
while True:
    answer = input("Select Mode 1, Mode 2 or Mode 3: ")
    if answer == "Mode 1":
        mode1()
        break
    elif answer == "Mode 2":
        mode2()
        break
    elif answer == "Mode 3":
        mode3()
        break
    else:
        print("Invalid mode selection. Please try again.")

# END
