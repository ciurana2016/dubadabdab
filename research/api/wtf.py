from getpass import getpass
from requests_html import HTMLSession


# Datos
email = 'admin@victorciurana.com'
# password = getpass('Password:')
LOGIN_URL = 'https://www.infojobs.net/'
# POST_DATA = {
#     'client_id': 'empleo_ij',
#     'login_url_type': 'WEB',
#     'login_type': '3',
#     'email': email,
#     'password': password,
# }
session = HTMLSession()

# Burp
proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
session.proxies.update(proxies)

r = session.post(url=LOGIN_URL, verify=False)
print('[*] About to render response')
r.html.render()
print('[*] Code rendered')
print(r.text)
# Render ... donde? osea wt

print('EOF')
