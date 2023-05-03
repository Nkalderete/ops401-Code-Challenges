#!/usr/bin/python3
# Nick Alderete
# Network Scanner
# Worked with Sierra, Geneva and Justin H.


# Import necessary modules
from scapy.all import *
import socket
import ipaddress
import sys 


# Define function for ICMP ping sweep
def sweep(network):
    # IP address of the target host
    network = ipaddress.IPv4Network(network)
    
    # Loop IP addresses on network
    for ip in network.hosts():
        response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)

        # Verify the response was received
        if response:
            if response[ICMP].code == 3:

                # Echo ICMP traffic is blocked by network
                print(f"{ip}: ICMP traffic blocked by network")

            else:
                # Display IP and ICMP code
                print(f"{ip}: {response[ICMP].code}")
                print("Network address of the network: ", network.network_address)
                print("Network mask: ", network.netmask)
                print("Total number of hosts under the network: ", network.num_addresses)
                print(f"({network}) is up")

                ip_network = ipaddress.IPv4Network(network)
                # Display the network mask from the IP address
                print(f"The network mask for {ip} is: ", ip_network.netmask)
                break
        else:
            print(f"No response from {ip}")

# Define function for ICMP ping sweep
def IPsweep(ip):
    # IP address of the target host
    IPa = ipaddress.IPv4Address(ip)

    # Wait for ICMP responses
    response = sr1(IP(dst=str(ip))/ICMP(), timeout=1, verbose=0)

    # Check if a response was received
    if response:
        if response[ICMP].code == 3:
            # Echo ICMP traffic is blocked by network
            print(f"{ip}: ICMP traffic blocked by network")
        # Display the IP address and ICMP code
        else:
            print(f"{IPa}: {response[ICMP].code}")
            print(f"({IPa}) is up")
            ip_network = ipaddress.ip_network(IPa)
            network_mask = ip_network.netmask
            print("The network mask is: ", network_mask)
    else:
        print(f"No response from {ip}")

# User menu
while True:
    user = input("\nPlease select one of the following:\n1. Port Scanner\n2. ICMP Scanner\n3. Exit\n\n")

    # Port scanner
    if user == "1":
        print("Entering Port Scanner Mode\n")
        # Get the IP address of the target host from user input
        ip_address = input("\nPlease enter an IP address to scan:\n")

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
 
    # ICMP sweep    
    if user == "2":
        print("Entering ICMP Scanner Mode\n")
        # Choices
        reply = input("1. IP\n2. Network\n3. Exit \n\n")
        # IP - IP of the place you want to scan
        if reply == "1":
            print("Selected- IP")
            ip = input("\nPlease type an IP address:\n")
            IPsweep(ip)
        # Nework - CIDR Block  
        if reply == "2": 
            print("Selected- Network")
            IPnetwork = input("\nPlease type a IP w/ CIDR:\n")
            sweep(IPnetwork)

        if user.lower() == "3":
            print("Exiting...")
            sys.exit()

    # Exit
    if user == "3":
        print("Exiting...")
        sys.exit()

# END 
