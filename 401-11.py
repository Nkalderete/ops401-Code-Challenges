#!/usr/bin/env python3
# Nick Alderete
# Network Scanner day 1


# Import necessary modules
from scapy.all import IP, sr1, TCP

# Get the IP address of the target host from user input
ip_address = input("Please enter an IP address to scan: ")

# Define the range of ports to scan
port_range = [22, 23, 80, 443, 3389]

# Get the source port number from user input
source_port = int(input("Enter source port number: "))

# Scan each port in the specified range using a loop
for port in port_range:
    # Send a SYN packet and wait for a response
    response = sr1(IP(dst=ip_address) / TCP(sport=source_port, dport=port, flags="S"), timeout=1, verbose=0)

    # If the response has a TCP layer
    if response and response.haslayer(TCP):
        # If the SYN-ACK flag is set, the port is open
        if response[TCP].flags == "SA":
            print(f"Port {port} is open")
        # If the RST flag is set, the port is closed
        elif response[TCP].flags == "RA":
            print(f"Port {port} is closed")
    # If no response was received
    else:
        print(f"No response received from {ip_address} for port {port}")
