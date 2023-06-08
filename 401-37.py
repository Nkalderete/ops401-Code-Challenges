#!/usr/bin/python3
# Nick Alderete
# Cookie Capture Capades


import requests
import webbrowser

# targetsite = input("Enter target site:")  # Uncomment this to accept user input target site
targetsite = "http://www.whatarecookies.com/cookietest.asp"  # Comment this out if you're using the line above

response = requests.get(targetsite)
cookie = response.cookies

print("Target site is " + targetsite)
print(cookie)

# Send the cookie back to the site and receive an HTTP response
new_response = requests.get(targetsite, cookies=cookie)

# Get the file path from the user
file_path = input("Enter the file path to save the HTML file: ")

# Generate an .html file to capture the contents of the HTTP response
page = new_response.text
with open(file_path, 'w') as file:
    file.write(page)

# Open the file with Firefox
webbrowser.get('firefox').open(file_path)
