import sys
import requests
from bs4 import BeautifulSoup

# fetch page title
def fetch_title(page):
    if page.title:
        return page.title.text
    return "No Title"


# fetch body text
def fetch_body(page):
    page_body = page.find("body")
    if page_body:
        return page_body.get_text(" ", strip=True)
    return "No Body"


# print all links from page
def print_links(page):
    links = page.find_all("a")
    for item in links:
        url = item.get("href")
        if url and url.startswith("http"):
            print(url)


# check command line input
if len(sys.argv) != 2:
    print("Please provide a URL")
    sys.exit(0)

website_url = sys.argv[1]

request_headers = {
    "User-Agent": "Mozilla/5.0"
}

# get webpage content
try:
    page_response = requests.get(website_url, headers=request_headers)
except:
    print("Unable to fetch the URL")
    sys.exit(0)

# parse webpage html
page_soup = BeautifulSoup(page_response.text, "html.parser")

# display output
print("Title:", fetch_title(page_soup))
print()
print("Body:")
print(fetch_body(page_soup))
print()
print("Outlinks:")
print_links(page_soup)