import requests
from bs4 import BeautifulSoup

test_url = 'https://developer.infojobs.net/test-console/execute.xhtml'

test_cookies = {
    'JSESSIONID' : 'DQee5njCmNvgiOWRTsbv2ZHO',   

}

r = requests.get(test_url, cookies=test_cookies)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

print('EOF')