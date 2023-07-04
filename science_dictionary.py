import requests
from bs4 import BeautifulSoup

query = "electron"
# Define the URL of the website
url = "https://www.thesciencedictionary.com/results/?q=" + query

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content of the response
soup = BeautifulSoup(response.content, "html.parser")


# Find all link elements with the specified class
link_elements = soup.find_all("a")

# Iterate over the link elements
for link_element in link_elements:
    # Get the text associated with each link
    link_text = link_element.text.strip()
    print("Link Text:", link_text)