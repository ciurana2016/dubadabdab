import requests
from bs4 import BeautifulSoup
from pprint import pprint


s = requests.Session()

### LOGIN ###

# LOGIN_URL = 'https://accounts.infojobs.net/security/accounts/login/run'
# email = 'admin@victorciurana.com'
password = input('Password:')

# post_data = {
#     'type': '0',
#     'j_clientId': 'developer-site-net',
#     'email': email,
#     'password': password,
#     'submit': 'Log In'
# }

# r = s.post(LOGIN_URL, data=post_data)
# print('Status code = %s' % r.status_code)

### LOGIN DONE ###


### TEST Get candidate data from api ###

# Primero validamos que damos permiso a esta peticion con nuestra cuenta
ACCESS_URL_01 = 'https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL'

access_url_01_headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Origin': 'https://www.infojobs.net',
    'Referer': 'https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36',
}

access_url_01_post_data = {
    'client_id': 'empleo_ij',
    'login_url_type': 'WEB',
    'login_type': '3',
    'email': 'admin@victorciurana.com',
    'password': password
}

r = s.post(ACCESS_URL_01, headers=access_url_01_headers, data=access_url_01_post_data)
print('Status code oauth? = %s' % r.status_code)
print('Oauth 1 response headers =')
pprint(s.headers)
pprint(s.cookies)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

# API_URL = 'https://developer.infojobs.net/test-console/execute.xhtml'

# form_data = {
#     'urifield': 'https://api.infojobs.net/api/2/candidate',
#     'versionfield': '2',
#     'methodfield': 'GET',
#     'hmethodfield': 'GET',
#     'operationEntityField': '-candidate',
#     'attachment_type': 'Local',
#     'paramsAttached': '1',
#     'headersAttached': '1',
#     'bodyContentType': 'json'
# }

# TODO: Usar Session
# r = s.post(API_URL, data=form_data, cookies=s.cookies)
# print('Status code segunda peticion = %s' % r.status_code)


# soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

### TEST DONE ! a programar robot ! ###
