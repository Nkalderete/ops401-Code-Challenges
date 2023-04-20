#!/usr/bin/python3
# Nick Alderete
# Worked with Sierra, Geneva and Justing H


# Uptime sensor pt. 2

# Import Libraries
import os
import datetime
import time
import smtplib
from getpass import getpass 



# Ask for email information
email = input("Please provide email address: ")
password = getpass("Please provide your password: ")

# Target IP
target = input("What is the target IP address?: ")

# Status messages
up = "Network is active"
down = "Network is down"

# Function
def ping_status(target):
    # Evaluate response and assign status
    response = os.system("ping -c 1 " + target)
    if response == 0:
        status = "Network is up"
    else:
        status = "Network is down" 
    return status 

# Sending status change email
def send_email(status):
    # SMTP session 
    s = smtplib.SMTP('smtp.gmail.com', 587)
    # Start TLS
    s.starttls()
    # Logging into email
    s.login(email, password)
    # Status message
    now = datetime.datetime.now()
    subject = f"TARGET NETWORK STATUS {status.lower()}"
    message = f"Your target server is {status.lower()} at {now.strftime('%Y-%m-%d %H:%M:%S')}"
    s.sendmail(email, email, message)
    # Close SMTP sesh
    s.quit()

# Ping status
last_status = ping_status(target)

# Ping every 2 senconds and send email if status changes
while True:
    current_status = ping_status(target)
    if current_status != last_status:
        send_email(current_status)
        last_status = current_status
    # 2 second lag between pings
    time.sleep(2)


