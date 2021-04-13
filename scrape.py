from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import re

req = Request('http://www.nuclearlaunchdetected.com/', headers={'User-Agent' : "Magic Browser"}) 
html_page = urlopen(req)

soup = BeautifulSoup(html_page, 'lxml')
links = []
for potential_link in soup.findAll('a', {'class':'sm2_button'}):
    links.append(potential_link.get('href'))

with open('links.txt', 'w+') as f:
    for link in links:
        f.write('%s\n' %link)