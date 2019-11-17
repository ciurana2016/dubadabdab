import requests
from bs4 import BeautifulSoup

test_url = 'https://developer.infojobs.net/test-console/execute.xhtml'


r = requests.get(test_url)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

print('EOF')