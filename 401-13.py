#!/usr/bin/python3
# Nick Alderete
# Network Scanner
# Worked with Sierra, Geneva and Justin H.


# Import necessary modules
from scapy.all import *
import socket
import ipaddress
import sys 
import time
import getmac

# Define function for port scanning
def port_scan(ip_address):
    # Define the range of ports to scan
    port_range = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3389]

    # Get the source port number from user input
    source_port = int(input("Enter source port number:\n"))

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

# Define function for ICMP ping sweep
def ping_sweep(ip_address):
    # Wait for ICMP responses
    response = sr1(IP(dst=ip_address)/ICMP(), timeout=1, verbose=0)

    # Check if a response was received
    if response:
        if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
            # Echo ICMP traffic is actively blocked by host
            print(f"{ip_address}: ICMP traffic blocked by host")
        else:
            # Display the IP address and ICMP code
            print(f"\nICMP code(s) for {ip_address} is: {response[ICMP].code}")
            print(f"Network ({ip_address}) is up")
            ip_network = ipaddress.ip_network(ip_address)
            network_mask = ip_network.netmask
            print(f"The network mask for ({ip_address}) is: ", network_mask )
            print("\n")

            # Call port scanning function if the host is responsive to ICMP echo requests
            port_scan(ip_address)
    else:
        print(f"\nNo response from {ip_address}\n")

def get_mac_address(ip_address):
    try:
        mac_address = getmac.get_mac_address(ip=ip_address)
        if mac_address is None:
            return "MAC address not found"
        else:
            return mac_address
    except:
        return "Error getting MAC address"

# User menu
while True:
    # Get the IP address of the target host from user input
    ip_address = input("\nPlease enter an IP address to scan:\n")

    # Call ICMP ping sweep function
    ping_sweep(ip_address)

    # Print network information for the IP address
    try:
        host = socket.gethostbyaddr(ip_address)[0]
        print(f"\nHostname: {host}\n")
    except:
        pass
    print(f"IP address: {ip_address}")
    print(f"NetBIOS name: {ipaddress.IPv4Address(ip_address).reverse_pointer}")
    print(f"MAC address: {get_mac_address(ip_address)}\n")
    
    # Prompt the user to continue or exit
    user_input = input("Press any key to continue scanning or 'q' to quit:\n")
    if user_input.lower() == "q":
        print("Exiting...")
        time.sleep (2)
        sys.exit()
    elif user_input:
        continue

# END