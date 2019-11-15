# encoding=utf8
'''
Testear cosas
'''
import requests
from bs4 import BeautifulSoup


# Url
url = 'https://www.infojobs.net/'
"""
USER_AGENT = ir a navegador abrir consola y poner navigator.userAgent
"""
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
headers = {'User-Agent': user_agent}
# Request
r = requests.get(url, headers=headers)      

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

print('EOF')