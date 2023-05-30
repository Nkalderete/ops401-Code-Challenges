#!/usr/bin/python3
# Nick Alderete
# Signature-based Malware Detection | 1 of 3


import os
import platform




# Prompt the user to type in a file name to search for
filename = input("Please enter the file name to search for: \n")

# Prompt the user for a directory to search in
directory = input("Please enter the directory to search in: \n")

# Search each file in the directory by name
def find_all_files(filename, directory):
    result = []
    for root, dirs, files in os.walk(directory):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result

# Call the function to search for the file
search_result = find_all_files(filename, directory)

# Display the search result
if search_result:
    print("This operating system is: \n", platform.system())
    print("Number of files searched: \n", len(search_result))
    print("Number of hits found: \n", len(search_result)) 
    print("==FILE INFORMATION==")

    for file_path in search_result:
        print(f"Target file: {filename} \nFile path:", file_path)
        
else:
    print("File not found.")
    print("Number of files searched: 0")
    print("Number of hits found: 0")
