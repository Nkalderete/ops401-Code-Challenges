#!/usr/bin/env python3
# Nick Alderete


import os
import datetime
import time
import logging




# Prompt user for target IP address
target = input("Enter the target IP address: ")

# Create and configure logger
logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Add console handler to print log messages to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)

# Log different log levels
logger.debug("DEBUGGING\n")
logger.info("INFORMATIONAL\n")
logger.warning("WARNING\n")
logger.error("ERROR\n")
logger.critical("!!CRITICAL!!\n")

while True:
    # Perform a single ping packet to the target
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
