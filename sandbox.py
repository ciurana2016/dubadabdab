# encoding=utf8
'''
Testear cosas
'''
import requests
from bs4 import BeautifulSoup


# Url
url = 'https://www.infojobs.net/'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
# Request
r = requests.get(url, headers=headers)      

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

print('EOF')