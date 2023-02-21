import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = []
for link in soup.find_all('a'):
    link_url = link.get('href')
    if link_url and link_url.startswith('http'):
        links.append(link_url)

print(links)
