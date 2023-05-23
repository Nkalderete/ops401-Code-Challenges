#!/usr/bin/env python3
# Nick Alderete



import logging
import os
import datetime
import time




target = input("Enter the target IP address: \n")


def ping_status(target):
    try:
        # Evaluate the response and assign success or failure to the status 
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "Successful ping."
            print(f"{target} is up and responding.")
        else:
            status = "Failed ping, check your IP address or network is down."
            print(f"{target} is not responding, try again later or check IP address.")
        
        # Get the current timestamp and print the status and timestamp
        current_time = datetime.datetime.now()
        print(f"{current_time} - Status: {status}")
        return status
    except Exception as e:
        logging.exception("An error occurred")
        raise e

# Create and configure logger
logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='w')

# Create object
logger = logging.getLogger()

# Setting the threshold
logger.setLevel(logging.DEBUG)

while True:
    try:
        # Transmit a single ICMP ping packet to the target
        ping_status(target)
        time.sleep(2)
        
    except KeyboardInterrupt:
        break
    
    except Exception as e:
        logging.exception("An error occurred")
