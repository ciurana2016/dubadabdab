import time
import requests
from bs4 import BeautifulSoup
from pprint import pprint




email = 'admin@victorciurana.com'
password = input('Password:')

# Me hago la picha un lio, necesito una cookie de sesion primero
# la siguiente url no esta capada por destil, la sacamos de alli.
# https://developer.infojobs.net/user/login/index.xhtml

s = requests.Session()

# Burp
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
s.proxies.update(proxies)

PRE_URL = 'https://developer.infojobs.net/user/login/index.xhtml'
PRE_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'developer.infojobs.net',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
}
r = s.get(PRE_URL, headers=PRE_HEADERS, verify=False)

# Tengo sesion en cookies y la peticion fue desde "chrome" !!!
# pprint(r.request.headers)
# pprint(s.cookies)
print('[*] Tenemos una cookie de sesion valida')
time.sleep(2) # Because


# Ahora que tenemos la cookie hacemos login como si fueramos un humano.

"""
    Estos salen en los headers pero no lo son en realidad, los omitimos
    ':authority': 'accounts.infojobs.net',
    ':method': 'POST',
    ':path': '/security/accounts/login/run',
    ':scheme': 'https',
"""
LOGIN_URL = 'https://accounts.infojobs.net/security/accounts/login/run'
LOGIN_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
    'content-length': '103',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://developer.infojobs.net',
    'referer': 'https://developer.infojobs.net/user/login/index.xhtml',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
LOGIN_FORM_DATA = {
    'type': '0',
    'j_clientId': 'developer-site-net',
    'email': email,
    'password': password,
    'submit': 'Log In',
}
r = s.post(LOGIN_URL, headers=LOGIN_HEADERS, data=LOGIN_FORM_DATA, cookies=s.cookies, verify=False)
# Su puta madre funciona LOL !!! 
# print(r.status_code)
# pprint(r.request.headers)
# pprint(s.cookies)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
print('[*] Login conseguido a web de la api')
time.sleep(2)

# Ahora hacemos una peticion que va a fallar a la API y que nos ha de devolver una cookie  de TEST algo.
FAIL_URL = 'https://developer.infojobs.net/test-console/execute.xhtml'
FAIL_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'es-ES,es;q=0.9,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '219',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'developer.infojobs.net',
    'Origin': 'https://developer.infojobs.net',
    'Referer': 'https://developer.infojobs.net/test-console/console.xhtml?operationEntityField=-candidate&methodfield=GET&versionfield=2',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}
FAIL_FORM_DATA = {
    'urifield': 'https://api.infojobs.net/api/2/candidate',
    'versionfield': '2',
    'methodfield': 'GET',
    'hmethodfield': 'GET',
    'operationEntityField': '-candidate',
    'attachment_type': 'Local',
    'paramsAttached': '1',
    'headersAttached': '1',
    'bodyContentType': 'json',
}
r = s.post(FAIL_URL, headers=FAIL_HEADERS, data=FAIL_FORM_DATA, cookies=s.cookies, verify=False)
# print(r.status_code)
# pprint(r.request.headers)
# pprint(s.cookies)
# soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())
print('[*] Primera peticion a la API fallada con exito')
time.sleep(2)






