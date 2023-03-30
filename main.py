import requests
from bs4 import BeautifulSoup
import os

# URL of the website to be scraped
url = "https://example.com/"

# Create a folder to save the scraped data
folder_name = "scraped_data"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Make a request to the website and retrieve the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup and extract the desired data
soup = BeautifulSoup(html_content, "html.parser")
# Example: Extract all images from the website and save them to the folder
img_tags = soup.find_all("img")
for img_tag in img_tags:
    img_url = img_tag["src"]
    img_data = requests.get(img_url).content
    with open(os.path.join(folder_name, os.path.basename(img_url)), "wb") as f:
        f.write(img_data)
