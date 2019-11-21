import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint


# Copiamos peticion de Burp FUNCIONA LOL



s = requests.Session()

# Burp
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
s.proxies.update(proxies)

BURP_URL = 'https://developer.infojobs.net/test-console/execute.xhtml'
BURP_HEADERS = {
    'Host': 'developer.infojobs.net',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '124',
    'Origin': 'https://developer.infojobs.net',
    'DNT': '1',
    'Connection': 'close',
    'Referer': 'https://developer.infojobs.net/test-console/console.xhtml?operationEntityField=-candidate&methodfield=GET&versionfield=2',
    'Upgrade-Insecure-Requests': '1',
}
BURP_COOKIES = {
    'JSESSIONID': 'zoHdJ1hD933NY77nl6ND+TCv',
    'AWSELB': '6F772D7F025CE724146F13F5B98B9A20F07F7A8E0C9BD186660F9C57B168BCE489D060DEB601CE8948C896AF7D4494949DBAB3487512C772A0F98AC9834E315B69561AC2CD'
}
BURP_POST_DATA = {
    'urifield': 'https://api.infojobs.net/api/2/candidate',
    'versionfield': '2',
    'methodfield': 'GET',
    'operationEntityField': '-candidate'
}
r = s.post(BURP_URL, headers=BURP_HEADERS, data=BURP_POST_DATA, cookies=BURP_COOKIES, verify=False)

# Tengo sesion en cookies y la peticion fue desde "chrome" !!!
pprint(r.request.headers)
pprint(s.cookies)
print('[*] burp')
time.sleep(2) # Because




