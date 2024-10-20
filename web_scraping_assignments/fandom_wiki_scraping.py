import requests
from bs4 import BeautifulSoup
import csv

import requests
from bs4 import BeautifulSoup
import json

# The URL of the page you want to scrape
url = "https://ultimatepopculture.fandom.com/wiki/University_of_Illinois_Urbana-Champaign"

# Send an HTTP request to get the page content
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Scrape the page title
page_title = soup.find('h1', class_='page-header__title').text.strip()

# Scrape all the infobox fields
infobox = soup.find('table', class_='infobox')
infobox_data = {}

for row in infobox.find_all('tr'):
    if row.th and row.td:
        key = row.th.text.strip()
        value = row.td.text.strip()
        infobox_data[key] = value

# Scrape the main content sections
main_content = []
for section in soup.find_all('p'):
    main_content.append(section.text.strip())

# Print the scraped data (for testing purposes)
print(f"Page Title: {page_title}")
print("\nInfobox Data:")
for key, value in infobox_data.items():
    print(f"{key}: {value}")

print("\nMain Content:")
for paragraph in main_content:
    print(paragraph)

# Save the data to a JSON file
data = {
    "page_title": page_title,
    "infobox_data": infobox_data,
    "main_content": main_content
}

with open('uiuc_data.json', 'w') as file:
    json.dump(data, file, indent=4)

print("All data has been saved to uiuc_data.json")
