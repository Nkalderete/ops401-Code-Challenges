#!/usr/bin/python3
# Nick Alderete
# Uptime sensor w/ logging 2 of 3




import logging
import os
import datetime
import time
import logging.handlers


def ping_status(target):
    try:
        # Check ping status and return success or failure
        icmp = os.system("ping -c 1 " + target)
        if icmp == 0:
            status = "Successful ping, network is responding.\n"
            print(f"{target} is up and responding.")
            # Log successful ping
            logger.info(f"\nIP address: {target} \nStatus: {status}")
        else:
            status = "Failed ping, check your IP address or network is down.\n"
            print(f"{target} is not responding, try again later or check IP address.")
            # Log failed ping
            logger.warning(f"\nIP address: {target} \nStatus: {status}")

        # Get the current timestamp and print the status and timestamp
        current_time = datetime.datetime.now()
        print(f"{current_time} - Status: {status}")
        return status
    except Exception as e:
        logger.exception("An error occurred")
        raise e


if __name__ == "__main__":
    target = input("Enter the target IP address: \n")

    # Create and configure logger
    logging.basicConfig(filename="Demo.log", format='%(asctime)s %(message)s', filemode='a')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    # Set log file and max file size
    log_file = 'Demo.log'
    max_size_bytes = 2 * 1024 * 1024  # 2MB

    # Create a file handler with log rotation
    file_handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=max_size_bytes, backupCount=5)
    file_handler.setLevel(logging.DEBUG)

    # Define the log format
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    while True:
        try:
            # Transmit a single ICMP ping packet to the target
            ping_status(target)
            time.sleep(2)
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.exception("An error occurred")
