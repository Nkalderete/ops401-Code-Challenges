#!/usr/bin/python3
# Nick Alderete
# Signature-based Malware Detection | 3 of 3



import os
import time
import platform
import hashlib
from datetime import datetime
import subprocess


# Prompt the user for a directory to search in
search_directory = input("Please enter the directory to search in: \n")
# Prompt the user for the API key and script path
api_key = input("Please enter your API Key: \n")
script_path = input("Please enter the file path of the VirusTotal script: \n")

# Add a time stamp
timestamp = datetime.now()

# Create .txt file for output information
output_file = open("DirectoryScan.txt", "w")

# Recursive function to search for files
def search_files(directory):
    search_result = []
    if os.path.isfile(directory):
        search_result.append(directory)
    elif os.path.isdir(directory):
        for root, dirs, files in os.walk(directory):
            for file_name in files:
                search_result.append(os.path.join(root, file_name))
    return search_result


# Calculate the MD5 hash for a file
def calculate_hash(file_path):
    # Hash object
    hasher = hashlib.md5()
    try:
        # Open file
        with open(file_path, 'rb') as file_obj:
            # Loop through the file content
            chunk = file_obj.read(1024)
            while chunk:
                hasher.update(chunk)
                chunk = file_obj.read(1024)
    except FileNotFoundError:
        return None
    return hasher.hexdigest()


# Calculate the file size
def get_file_size(file_path):
    try:
        return os.path.getsize(file_path)
    except FileNotFoundError:
        return None


# Call the function to search for the files
search_result = search_files(search_directory)


# Display the search result
if search_result:
    # Print system statistics
    print("")
    print("== System Statistics ==")
    print("Current operating system:", platform.system())
    print("Number of files searched:", len(search_result))
    print("Number of hits found:", len(search_result))
    print("Timestamp:", timestamp)
    print('---------------')
    time.sleep(2)

    # Write system statistics to the output file
    output_file.write("== System Statistics ==")
    output_file.write("\nCurrent operating system: " + platform.system() + "\n")
    output_file.write("Number of files searched: " + str(len(search_result)) + "\n")
    output_file.write("Number of hits found: " + str(len(search_result)) + "\n")
    output_file.write("Timestamp: " + str(timestamp) + "\n")
    output_file.write("---------------")
    time.sleep(2)

    # Print and write file details
    print(f"\nFiles found in given directory: {search_directory}:\n")
    time.sleep(1)
    output_file.write(f"\n== Files found in given directory: {search_directory} ==\n")

    for file_path in search_result:
        file_hash = calculate_hash(file_path)
        file_size = get_file_size(file_path)
        if file_hash is not None:
            print("File name:", os.path.basename(file_path))
            print("File path:", file_path)
            print("File size:", file_size)
            print("Hash:", file_hash)
            print("Timestamp:", timestamp)
            print('---------------')
            time.sleep(0.75)

            output_file.write("File name: " + os.path.basename(file_path) + "\n")
            output_file.write("File path: " + file_path + "\n")
            output_file.write("File size: " + str(file_size) + "\n")
            output_file.write("Hash: " + file_hash + "\n")
            output_file.write("Timestamp: " + str(timestamp) + "\n")
            output_file.write('---------------\n')
            
        else:
            print("Error calculating hash for file:", file_path)


    # Pass hashes to VirusTotal
    command = ['python3', script_path, '-k', api_key]
    for file_hash in map(calculate_hash, search_result):
        if file_hash is not None:
            command.extend(['-m', file_hash])

    # Execute the command
    subprocess.call(command)

else:
    output_file.write("No items found in the specified directory.\n")

# Close the output file
output_file.close()
