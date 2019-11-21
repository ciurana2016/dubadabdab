import re
import time
import requests

from random import randint, choice
from bs4 import BeautifulSoup



'''
    00 --> devuelve el html con js
    01 --> hacemos peticion del js, como si hicieramos la peticion al haber descargado el html primero
    02 --> POST la hueya digital, nos da cookies
    03 --> GET con las cookies, devuelve un OK 302 y supuestamente ya tira solo al final 
    
    Entre peticion y peticion cambiar referer.

'''

# UTILIDAD

def info(s):
    print('[*] DesTest | %s' % s)

def sleep():
    r = randint(0, 3)
    info('Sleeping %s seconds' % r)
    time.sleep(r)

def get_path_from_js(t):
    match = re.search(r'path:\"\/.+\.js\?PID=.+\",a', t)
    path = match.group()
    path = path.replace('path:"','').replace('",a','')
    if match:
        info('POST path found %s' % path)
        return path
    else:
        info('Something went wrong get_path_from_js, exiting')
        exit()

def get_ajax_header_from_js(t):
    match = re.search(r'ajax_header:\".+\",in', t)
    ajax_header = match.group()
    ajax_header = ajax_header.replace('ajax_header:"','').replace('",in','')
    if match:
        info('ajax header found %s' % ajax_header)
        return ajax_header
    else:
        info('Something went wrong get_ajax_header_from_js, exiting')
        exit()

def random_string(i):
    chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
    return ''.join([choice(chars) for _ in range(i)])

def generar_hueya_digital():
    # Proof
    rs1 = random_string(3)
    rs2 = random_string(20)
    millis = int(round(time.time() * 1000))
    proof = rs1 + ':' + millis + ':' + rs2

    # Devices
    devices = {
        'count': 6,
        'data': {}
    }
    for _ in range(6):
        kind = 'videoinput' if _ == 0 else 'audioinput'
        devices['data'][_] = {
            'deviceId': random_string(43)+'=',
            'kind': kind,
            'label': '',
            'groupId': random_string(43)+'='
        }
    from pprint import pprint
    pprint(devices)
    print(proof)

def main():
    s = requests.Session()
    # Provisional, pasar por Burp, o para debug
    # proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
    # s.proxies.update(proxies)

    # Primera peticion inicial
    url_00 = 'https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL'
    headers_00 = {
        'Host': 'www.infojobs.net',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'close',
        'Referer': 'https://developer.infojobs.net/',
        'Upgrade-Insecure-Requests': '1'
    }
    s.headers.update(headers_00)
    info('Peticion 00')
    r = s.get(url_00, verify=False)

    # Sacamos el archivo js que tenemos que descargar
    soup = BeautifulSoup(r.text, 'html.parser')
    js_to_download = ''
    for script in soup.find_all('script'):
        if script.get('src') != None:
            js_to_download = script.get('src')

    info('el script es %s' % js_to_download)

    # Segunda peticion
    url_01 = 'https://www.infojobs.net' + js_to_download
    r = s.get(url_01, verify=False)

    # Sacamos los datos que necesitamos de esta peticion para hacer la siguiente
    url_02 = get_path_from_js(r.text)
    ajax_header = get_ajax_header_from_js(r.text)
    hueya_digital = generar_hueya_digital()



# MAIN SHIT
if __name__ == '__main__':
    info('Starting')
    main()
    info('EOF')
