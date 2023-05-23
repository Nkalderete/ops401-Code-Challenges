#!/usr/bin/python3
# Nick Alderete



import os
import datetime
import time
# from datetime import datetime

target = input("Enter target IP address: \n")

while True:
    # Preform a single ping packet to the target
    response = os.system("ping -c 1 " + target)

    # Evaluate the response and assign success or failure to the status variable
    if response == 0:
        status = "Success"
    else:
        status = "Failure"

    # Get the current timestamp and print the status and timestamp
    current_time = datetime.datetime.now()
    print(f"{current_time} - Status: {status}")
    
    # Wait for 2 seconds before transmitting another ping packet
    time.sleep(2)
