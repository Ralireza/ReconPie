import requests

# Replace "https://www.example.com" with the URL of the webpage you want to check the status of
url = "https://hackerone.com"

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Check the HTTP status code of the response
if response.status_code == 200:
    print("Success!")
elif response.status_code == 404:
    print("Page not found.")
elif response.status_code == 500:
    print("Internal server error.")
else:
    print("Unknown status code:", response.status_code)


