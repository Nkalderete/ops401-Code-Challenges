#!/usr/bin/env python3
# Nick Alderete



import logging
import os
import datetime
import time



target = input("Enter the target IP address: \n")


# Create and configure logger
logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def ping_status(target):
    try:
        # Check ping status and return success or failure
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "Successful ping, network is responding."
            print(f"{target} is up and responding.")
            #Log successful ping
            logger.info(f"\nIP address: {target} \nStatus: {status}")  
        else:
            status = "Failed ping, check your IP address or network is down."
            print(f"{target} is not responding, try again later or check IP address.")
            # Log failed ping
            logger.warning(f"\nIP address: {target} \nStatus: {status}")  
        
        # Get the current timestamp and print the status and timestamp
        current_time = datetime.datetime.now()
        print(f"{current_time} - Status: {status}")
        return status
    except Exception as e:
        logging.exception("An error occurred")
        raise e

while True:
    try:
        # Transmit a single ICMP ping packet to the target
        ping_status(target)
        time.sleep(2)
    except KeyboardInterrupt:
        break
    except Exception as e:
        logging.exception("An error occurred")
