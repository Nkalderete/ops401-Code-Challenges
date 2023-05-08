#!/usr/bin/python3
# Nick Aldereet
# Worked with Geneva and Sierra


import time

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

# User menu
while True:
    answer = input("Select Mode 1 or Mode 2: ")
    if answer == "Mode 1":
        mode1()
        break
    elif answer == "Mode 2":
        mode2()
        break
    else:
        print("Invalid mode selection. Please try again.")
