# Import the necessary libraries
import requests
import json

# Define the URL of the target website
url = "https://www.example.com"

# Define the list of functions to scan for
functions = ["login", "signup", "search", "checkout"]

# Send a GET request to the website and store the response
response = requests.get(url)

# Check if the response is successful
if response.status_code == 200:
    # Parse the response body as JSON
    body = json.loads(response.text)

    # Loop through the list of functions
    for function in functions:
        # Check if the current function is present in the response body
        if function in body:
            print(f"{function} function found!")
else:
    print("Error: Unable to retrieve response from website.")
