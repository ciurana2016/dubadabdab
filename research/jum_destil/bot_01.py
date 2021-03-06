import requests

from getpass import getpass
from pwned import jump_destil



print('[*] Bot start')

s = requests.Session()

# Burp
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
s.proxies.update(proxies)

# Saltamos cortafuegos
s = jump_destil(s, 'https://www.infojobs.net')
print('[*] Cortafuegos saltado')

# Primera peticion
url = 'https://developer.infojobs.net/test-console/console.xhtml'
s.headers['Host'] = 'developer.infojobs.net'
r = s.get(url, verify=False)
print('[*] Primera peticion ok')

# Login developer site
password = getpass('Password:')
email = 'admin@victorciurana.com'
url = 'https://accounts.infojobs.net/security/accounts/login/run'
login_form_data = {
    'type': '0',
    'j_clientId': 'developer-site-net',
    'email': email,
    'password': password,
    'submit': 'Log In',
}
del s.headers['Host']
r = s.post(url, data=login_form_data, verify=False)
print('[*] Logeado correctamente')

# Peticion a la "API"
url = 'https://developer.infojobs.net/test-console/execute.xhtml'
api_form_data = {
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
r = s.post(url, data=api_form_data, verify=False)
print('[*] Primer POST que falla apsta contra API')

# Login permisos api
# https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL
# [1] Peticion fantasma por si acaso
scopes = 'MY_APPLICATIONS,CANDIDATE_PROFILE_WITH_EMAIL'
url = 'https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope='+scopes+'&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state='+scopes
r = s.get(url, verify=False)
# [2] Ara si login
url = 'https://accounts.infojobs.net/security/accounts/login/run'
#s.headers['referer'] = 'https://www.infojobs.net/api/api-login/api-login.xhtml?client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&scope=CANDIDATE_PROFILE_WITH_EMAIL'
api_login_data = {
    'client_id': 'empleo_ij',
    'login_url_type': 'WEB',
    'login_type': '3',
    'email': email,
    'password': password
}
r = s.post(url, data=api_login_data, verify=False)

# [3] Clickar en Aceptar
url = 'https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?user_oauth_approval=true&auth_type=api&scopes='+scopes
api_approval_data = {
    'client_id': 'devsite-test-console-net',
    'redirect_uri': 'https://developer.infojobs.net/test-console/continue-request.xhtml'
}
r = s.post(url, data=api_approval_data, verify=False)
print('[*] Permisos a la api dados para -candidate')

# Peticion a la "API"
url = 'https://developer.infojobs.net/test-console/execute.xhtml'
api_form_data = {
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
r = s.post(url, data=api_form_data, verify=False)

print('EOF')
