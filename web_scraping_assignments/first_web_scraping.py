import requests
from bs4 import BeautifulSoup

url = "https://www.gutenberg.org/browse/scores/top"  
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

top_100_section = soup.find('h2', string="Top 100 EBooks yesterday")
if top_100_section:
    top_100_list = top_100_section.find_next('ol')

    for li in top_100_list.find_all('li'):
        print(li.get_text())
else:
    print("Could not find the 'Top 100 EBooks yesterday' section")
