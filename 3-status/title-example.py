import requests
from bs4 import BeautifulSoup

# Replace "https://www.example.com" with the URL of the webpage you want to extract the title from
url = "https://hackerone.com"

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Use Beautiful Soup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Extract the title of the webpage using the 'title' tag
title = soup.title.string

print(title)