import requests
from bs4 import BeautifulSoup

class HtmlMining:
    def get_title(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string
        print(f"the title of url {url} is {title}")
        return title
    
    def get_content(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        content = soup.get_text()
        print(f"the content of url {url} is {content}")
        return content

    def get_status(url):
        # Send a GET request to the URL and store the response in a variable
        response = requests.get(url)
    
        # Check the HTTP status code of the response
        if response.status_code == 200:
            return "Success!"
        elif response.status_code == 404:
            return "Page not found."
        elif response.status_code == 500:
            return "Internal server error."
        else:
            return f"Unknown status code: {response.status_code}"
    
    def get_links(url):
        # Send a GET request to the URL and store the response in a variable
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a')
        print(f"the links of url {url} is {links}")
        return links
 
