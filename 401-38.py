#!/usr/bin/python3
# Nick Alderete
# XSS Vulnerability Detection with Python


# Author:      Abdou Rockikz
# Description: TODO: XSS Vulnerability Detection with Python
# Date:        TODO: 08Jun2023
# Modified by: TODO: Nick Alderete

# Import libraries
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# Declare functions

### TODO: Add function explanation here ###
### Takes input from the user and retrieves all the HTML forms, then returns a list of form elements
def get_all_forms(url):
    # Send a GET request to the URL. .content is used to access the raw content of the response
    # bs creates an object "soup" which is parsed HTML
    soup = bs(requests.get(url).content, "html.parser")
    # Return a list of all the form elements found in the HTML
    return soup.find_all("form")

### TODO: Add function explanation here ###
### This function extracts details from the 'form' variable. It returns a dictionary containing these form details
def get_form_details(form):
    # Empty dictionary to store form details
    details = {}
    # Save the form's attributes or 'attrs'. The 'get' method is used to access the form.
    # 'lower' converts the data to lowercase
    action = form.attrs.get("action").lower()
    # Retrieve the value of the method from the form element list. If no method is specified, default to "get".
    # Also converts the data to lowercase
    method = form.attrs.get("method", "get").lower()
    # Start a new empty list to store data
    inputs = []
    # Iterate over all input tags
    for input_tag in form.find_all("input"):
        # Retrieve the value of the type attribute of the input tag. If no type is specified, default to "text".
        input_type = input_tag.attrs.get("type", "text")
        # Retrieve the value of the name attribute of the input tag
        input_name = input_tag.attrs.get("name")
        # Create a dictionary with the input type and name, and append it to the 'inputs' list
        inputs.append({"type": input_type, "name": input_name})
    # Store the action URL in the dictionary
    details["action"] = action
    # Store the method (GET or POST) in the dictionary
    details["method"] = method
    # Store the inputs in the dictionary
    details["inputs"] = inputs
    # Return the details dictionary
    return details

### TODO: Add function explanation here ###
# This function constructs the form submission URL and populates the form fields with the provided data
# Either through GET or POST
def submit_form(form_details, url, value):
    # Use urljoin to join the base URL with the value of the action attribute
    target_url = urljoin(url, form_details["action"])
    # Retrieve the list of input fields from form_details and assign it to a new variable
    inputs = form_details["inputs"]
    # Create a new empty dictionary to store data
    data = {}
    # Iterate over each input in the inputs list
    for input in inputs:
        # Check if the input type is "text" or "search"
        if input["type"] == "text" or input["type"] == "search":
            # Assign the provided value to the value attribute to inject the value into the input field
            input["value"] = value
        # Get the value of the name attribute
        input_name = input.get("name")
        # Get the value of the value attribute
        input_value = input.get("value")
        # If both input_name and input_value are not None, continue with the script
        if input_name and input_value:
            # Add the name-value pair to the data dictionary
            data[input_name] = input_value
    # Check if the method is "post". This line sends a POST request to the target URL with the data included.
    if form_details["method"] == "post":
        # Return the response of the POST request
        return requests.post(target_url, data=data)
    else:
        # If the form method is not "post", send a GET request with the data as parameters
        return requests.get(target_url, params=data)


### TODO: Add function explanation here ###
# Main function that performs the XSS scan
# Takes a URL and scans for potential XSS vulnerabilities
# Returns True if a vulnerability is found, False otherwise
def scan_xss(url):

    # Call the get_all_forms function and assign the result to the 'forms' variable
    forms = get_all_forms(url)
    # Print a message indicating the number of forms detected
    print(f"[+] Detected {len(forms)} forms on {url}.")

    # Assign a JavaScript payload to a variable that triggers an alert
    js_script = "<script>alert('XSS Vulnerability');</script>"

    # Initialize a boolean variable to track whether any threats are found
    is_vulnerable = False

    # Loop that iterates over each form in the forms list
    for form in forms:
        # Call the get_form_details function to retrieve the details of the current form
        # Return the data as the 'form_details' variable
        form_details = get_form_details(form)
        # Call the submit_form function and assign its result to the 'content' variable
        content = submit_form(form_details, url, js_script).content.decode()
        # Check if the payload (js_script) is present in the content string. If found, continue with the script
        if js_script in content:
            # Print a message indicating that an XSS vulnerability was detected
            print(f"[+] XSS Detected on {url}")
            # Print a string before printing the form details
            print(f"[*] Form details:")
            # Print the form details using pprint (pretty print)
            pprint(form_details)
            # Indicate that an XSS vulnerability was found
            is_vulnerable = True
    # Return the is_vulnerable variable. True if a vulnerability was found, False otherwise
    return is_vulnerable

# Main

### TODO: Add main explanation here ###
# Prompt the user to enter a URL and call scan_xss to test for vulnerabilities
if __name__ == "__main__":
    # Prompt the user to enter a URL
    url = input("Enter a URL to test for XSS:")
    # Call the scan_xss function, passing the url as an argument
    print(scan_xss(url))





# OUTPUT EXAMPLES:
# Positive Detection (XSS vulnerability found):
# [+] Detected 1 forms on http://example.com.
# [+] XSS Detected on http://example.com
# [*] Form details:
# {'action': '/submit',
#  'inputs': [{'name': 'username', 'type': 'text'},
#             {'name': 'password', 'type': 'password'},
#             {'name': 'submit', 'type': 'submit'}],
#  'method': 'post'}
# True

# Negative Detection (No XSS vulnerability found):
# [+] Detected 2 forms on http://example.com.
# False
