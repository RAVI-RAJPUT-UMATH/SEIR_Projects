import sys
import requests
from bs4 import BeautifulSoup

# Function to get title
def get_title(soup):
    if soup.title:
        return soup.title.text
    else:
        return "No Title"


# Function to get body
def get_body(soup):
    if soup.body:
        return soup.body.get_text(separator=" ", strip=True)
    else:
        return "No Body"


# Function to get links
def get_links(soup):
    links = []
    for link in soup.find_all("a"):
        href = link.get("href")
        if href:
            links.append(href)
    return links


# Main Program 
if len(sys.argv) != 2:
    print("Usage: python seir.py <URL>")
    sys.exit()

url = sys.argv[1]
header = {'User-Agent': 'Mozilla/5.0'}

# Fetch webpage
try:
    response = requests.get(url, headers=header)
except:
    print("Error fetching the URL")
    sys.exit()

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Call functions
title = get_title(soup)
body = get_body(soup)
links = get_links(soup)

# Print output
print("Title page :", title)
print("Body page :", body)
print("ALL Links :")
print(" ".join(links))


# '''
# PS C:\Users\Lenovo\OneDrive\Desktop\coding\SEM 4\SEIR_Python_project> python scraper.py https://example.com
# Title page : Example Domain
# Body page : Example Domain This domain is for use in documentation examples without needing permission. Avoid use in operations. Learn more
# ALL Links :
# https://iana.org/domains/example
# PS C:\Users\Lenovo\OneDrive\Desktop\coding\SEM 4\SEIR_Python_project> python .\scraper.py https://univ.sitare.org/
# Title page : Sitare University Program
# Body page : You need to enable JavaScript to run this app.
# ALL Links :
# '''