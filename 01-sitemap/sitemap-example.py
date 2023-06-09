# pip install beautifulsoup4
from bs4 import BeautifulSoup

# pip install requests
import requests

def get_links(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML response using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Find all the links on the page
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        
        # Ignore links that are not URLs
        if href is not None and href.startswith("http"):
            links.append(href)
            
    return links

def crawl_site(url, depth=2):
    # Dictionary to store the site map
    site_map = {}
    
    # Recursive function to crawl the site and generate the sitemap
    def crawl(url, current_depth):
        # Stop crawling if we have reached the maximum depth specified
        if current_depth > depth:
            return
        
        # Get all the links on the current page
        links = get_links(url)
        
        # Add the links to the site map
        site_map[url] = links
        
        # Crawl each link recursively
        for link in links:
            if link not in site_map:
                crawl(link, current_depth + 1)
    
    # Call the crawl function to generate the site map
    crawl(url, 0)
    
    return site_map

# Example usage: Generate a site map for http://example.com with a maximum depth of 2
site_map = crawl_site("https://hackerone.com", depth=2)

# Print the site map
for url, links in site_map.items():
    print(url)
    for link in links:
        print("\t", link)
