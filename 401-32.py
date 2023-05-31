#!/usr/bin/python3
# Nick Alderete
# Signature-based Malware Detection | 2 of 3


import os
import hashlib
from datetime import datetime




def scan_directory(path):
    with open("DirScan.txt", "w") as f:
        for root, dirs, files in os.walk(path):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                md5_hash = generate_md5_hash(file_path)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                # Print files to screen 
                print("File Name:", file)
                print("Timestamp:", timestamp)
                print("File Size:", file_size, "bytes")
                print("Complete File Path:", file_path)
                print("MD5 Hash:", md5_hash)
                print("--------------------\n")
                
                # Write file info to DirScan file that was created
                f.write("File Name: " + file + "\n")
                f.write("Timestamp: " + timestamp + "\n")
                f.write("File Size: " + str(file_size) + " bytes\n")
                f.write("Complete File Path: " + file_path + "\n")
                f.write("MD5 Hash: " + md5_hash + "\n")
                f.write("--------------------\n")

# Generate md5 hash
def generate_md5_hash(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        md5_hash = hashlib.md5(data).hexdigest()
        return md5_hash

# Send it
directory_path = input("Enter the directory path to scan: ")
scan_directory(directory_path)
