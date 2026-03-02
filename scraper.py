import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# URL is given or not 
if len(sys.argv) != 2:
    print("Please provide a URL")
    sys.exit()

url = sys.argv[1]

# chrome settings
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# open browser
browser = webdriver.Chrome(options=chrome_options)
browser.get(url)

# give page some time to load javascript
time.sleep(3)

# print title
print("Title:", browser.title)

# print body text
print("\nBody:")
try:
    page_body = browser.find_element(By.TAG_NAME, "body")
    print(page_body.text)
except:
    print("No Body")

# print links
print("\nOutlinks:")
all_links = browser.find_elements(By.TAG_NAME, "a")
for item in all_links:
    link = item.get_attribute("href")
    if link:
        print(link)

# close browser
browser.quit()