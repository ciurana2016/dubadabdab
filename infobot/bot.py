# -*- coding: utf-8 -*-

import os
import re
import json
import time
import urllib3
import requests

from random import uniform, choice
from getpass import getpass
from bs4 import BeautifulSoup
from colorama import Fore, Style



def info_login(email, password, session):

    s = session

    # Primera peticion
    url = 'https://developer.infojobs.net/test-console/console.xhtml'
    s.headers['Host'] = 'developer.infojobs.net'
    r = s.get(url, verify=False)

    # Login developer site
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

    # Login permisos api
    # https://www.infojobs.net/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL
    # [1] Peticion fantasma por si acaso
    scopes = 'MY_APPLICATIONS,CANDIDATE_PROFILE_WITH_EMAIL,CV'
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

def jump_distil(session, url_inicial):

    """
    session ==> sesion de requests
    url_inicial ==> https://www.undominio.com

    Una unica funcion para generar las cookies necesarias para sobrepasar
    el sistema antibots de destil networks.

    Basicamente hacemos una serie de peticiones iniciales, generamos una
    huella digital falsa y la enviamos para recibir cookies con las que
    poder navegar libremente, aparte de headers especificos.
    """

    # Quitar warnings de consola
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    if 'http' not in url_inicial and 'https' not in url_inicial:
        print('PON HTTPS EN LA PUTA URL NO NO FUNCIONA')
        exit()

    plantilla_huella_digital = {
        "cookies":1,
        "setTimeout":0,
        "setInterval":0,
        "appName":"Netscape",
        "platform":"MacIntel",
        "syslang":"es-ES",
        "userlang":"es-ES",
        "cpu":"IntelMacOSX10.14",
        "productSub":"20100101",
        "plugins": {
            "0": "ShockwaveFlash21.0.0.226"
        }
        ,
        "mimeTypes": {
            "0": "FutureSplashPlayerapplication/futuresplash", "1": "ShockwaveFlashapplication/x-shockwave-flash"
        }
        ,
        "screen": {
            "width": 1920, "height": 1080, "colorDepth": 24
        }
        ,
        "fonts": {
            "0": "HoeflerText", "1": "Monaco", "2": "Georgia", "3": "TrebuchetMS", "4": "Verdana", "5": "AndaleMono", "6": "Monaco", "7": "CourierNew", "8": "Courier"
        }
        ,
        "fp2": {
            "userAgent": "Mozilla/5.0(Macintosh;IntelMacOSX10.14;rv:70.0)Gecko/20100101Firefox/70.0", "language":"es-ES", "screen": {
                "width": 1920, "height": 1080, "availHeight": 1080, "availWidth": 1920, "pixelDepth": 24, "innerWidth": 1132, "innerHeight": 890, "outerWidth": 1132, "outerHeight": 964, "devicePixelRatio": 1
            }
            ,
            "timezone":1,
            "indexedDb":'true',
            "addBehavior":'false',
            "openDatabase":'false',
            "cpuClass":"unknown",
            "platform":"MacIntel",
            "doNotTrack":"1",
            "plugins":"ShockwaveFlash::ShockwaveFlash21.0r0::application/x-shockwave-flash~swf,application/futuresplash~spl",
            "canvas": {
                "winding": "yes", "towebp": 'false', "blending": 'true', "img": "728ddc481d62ea90224059266da144480bb41ee2"
            }
            ,
            "webGL": {
                "img": "8d37e15cc9363584537e76e4d202a7e8e811da59", "extensions": "ANGLE_instanced_arrays;EXT_blend_minmax;EXT_color_buffer_half_float;EXT_float_blend;EXT_frag_depth;EXT_shader_texture_lod;EXT_sRGB;EXT_texture_compression_rgtc;EXT_texture_filter_anisotropic;OES_element_index_uint;OES_standard_derivatives;OES_texture_float;OES_texture_float_linear;OES_texture_half_float;OES_texture_half_float_linear;OES_vertex_array_object;WEBGL_color_buffer_float;WEBGL_compressed_texture_s3tc;WEBGL_compressed_texture_s3tc_srgb;WEBGL_debug_renderer_info;WEBGL_debug_shaders;WEBGL_depth_texture;WEBGL_draw_buffers;WEBGL_lose_context", "aliasedlinewidthrange": "[1,1]", "aliasedpointsizerange": "[1,255.875]", "alphabits": 8, "antialiasing": "yes", "bluebits": 8, "depthbits": 24, "greenbits": 8, "maxanisotropy": 16, "maxcombinedtextureimageunits": 80, "maxcubemaptexturesize": 8192, "maxfragmentuniformvectors": 1024, "maxrenderbuffersize": 8192, "maxtextureimageunits": 16, "maxtexturesize": 8192, "maxvaryingvectors": 32, "maxvertexattribs": 16, "maxvertextextureimageunits": 16, "maxvertexuniformvectors": 1024, "maxviewportdims": "[16384,16384]", "redbits": 8, "renderer": "Mozilla", "shadinglanguageversion": "WebGLGLSLES1.0", "stencilbits": 0, "vendor": "Mozilla", "version": "WebGL1.0", "vertexshaderhighfloatprecision": 23, "vertexshaderhighfloatprecisionrangeMin": 127, "vertexshaderhighfloatprecisionrangeMax": 127, "vertexshadermediumfloatprecision": 23, "vertexshadermediumfloatprecisionrangeMin": 127, "vertexshadermediumfloatprecisionrangeMax": 127, "vertexshaderlowfloatprecision": 23, "vertexshaderlowfloatprecisionrangeMin": 127, "vertexshaderlowfloatprecisionrangeMax": 127, "fragmentshaderhighfloatprecision": 23, "fragmentshaderhighfloatprecisionrangeMin": 127, "fragmentshaderhighfloatprecisionrangeMax": 127, "fragmentshadermediumfloatprecision": 23, "fragmentshadermediumfloatprecisionrangeMin": 127, "fragmentshadermediumfloatprecisionrangeMax": 127, "fragmentshaderlowfloatprecision": 23, "fragmentshaderlowfloatprecisionrangeMin": 127, "fragmentshaderlowfloatprecisionrangeMax": 127, "vertexshaderhighintprecision": 0, "vertexshaderhighintprecisionrangeMin": 24, "vertexshaderhighintprecisionrangeMax": 24, "vertexshadermediumintprecision": 0, "vertexshadermediumintprecisionrangeMin": 24, "vertexshadermediumintprecisionrangeMax": 24, "vertexshaderlowintprecision": 0, "vertexshaderlowintprecisionrangeMin": 24, "vertexshaderlowintprecisionrangeMax": 24, "fragmentshaderhighintprecision": 0, "fragmentshaderhighintprecisionrangeMin": 24, "fragmentshaderhighintprecisionrangeMax": 24, "fragmentshadermediumintprecision": 0, "fragmentshadermediumintprecisionrangeMin": 24, "fragmentshadermediumintprecisionrangeMax": 24, "fragmentshaderlowintprecision": 0, "fragmentshaderlowintprecisionrangeMin": 24, "fragmentshaderlowintprecisionrangeMax": 24, "unmaskedvendor": "IntelInc.", "unmaskedrenderer": "IntelIrisOpenGLEngine"
            }
            ,
            "touch": {
                "maxTouchPoints": 0, "touchEvent": 'false', "touchStart": 'false'
            }
            ,
            "video": {
                "ogg": "probably", "h264": "probably", "webm": "probably"
            }
            ,
            "audio": {
                "ogg": "probably", "mp3": "maybe", "wav": "probably", "m4a": "maybe"
            }
            ,
            "vendor":"",
            "product":"Gecko",
            "productSub":"20100101",
            "browser": {
                "ie": 'false', "chrome": 'false', "webdriver": 'false'
            }
            ,
            "window": {
                "historyLength": 2, "hardwareConcurrency": 2, "iframe": 'false', "battery": 'false'
            }
            ,
            "location": {
                "protocol": "https:"
            }
            ,
            "fonts":""
        }
    }

    def get_path_from_js(t):
        match = re.search(r'path:\"\/.+\.js\?PID=.+\",a', t)
        path = match.group()
        path = path.replace('path:"','').replace('",a','')
        path = url_inicial + path
        if match:
            return path
        else:
            exit()

    def get_ajax_header_from_js(t):
        match = re.search(r'ajax_header:\".+\",in', t)
        ajax_header = match.group()
        ajax_header = ajax_header.replace('ajax_header:"','').replace('",in','')
        if match:
            return ajax_header
        else:
            exit()

    def random_string(i):
        chars = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        return ''.join([choice(chars) for _ in range(i)])

    def generar_huella_digital():
        # Proof
        rs1 = random_string(3)
        rs2 = random_string(20)
        millis = int(round(time.time() * 1000))
        proof = rs1 + ':' + str(millis) + ':' + rs2

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
        huella_digital = plantilla_huella_digital
        huella_digital['proof'] = proof
        huella_digital['devices'] = devices

        return huella_digital

    headers = {
        'Host': url_inicial.replace('https://',''),
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate',
        'DNT': '1',
        'Connection': 'close',
        'Upgrade-Insecure-Requests': '1'
    }
    session.headers.update(headers)
    r = session.get(url_inicial, verify=False)

    # Sacamos el archivo js que tenemos que descargar
    soup = BeautifulSoup(r.text, 'html.parser')
    js_to_download = ''
    for script in soup.find_all('script'):
        if script.get('src') != None:
            js_to_download = script.get('src')

    # Segunda peticion
    url = url_inicial + js_to_download
    r = session.get(url, verify=False)

    # Sacamos los datos que necesitamos de esta peticion para hacer la siguiente
    url_02 = get_path_from_js(r.text)
    ajax_header = get_ajax_header_from_js(r.text)
    huella_digital = generar_huella_digital()
    # Actualizamos headers
    headers['X-Distil-Ajax'] = ajax_header
    session.headers.update(headers)
    # Datos para POST
    post_data = {'p': str(huella_digital).replace("'",'"')}
    # Enviamos la peticion
    r = session.post(url_02, data=post_data, verify=False)
    xuid = r.headers['X-UID']

    # Ultimo get manual ?
    url_03 = url_inicial + '/distil_identify_cookie.html?httpReferrer=/'
    url_03 += '&uid=' + xuid
    r = session.get(url_03, verify=False)

    return session

def output(text, color, nostar=False):
    front = '[*] ' if nostar == False else ''
    text_output = front + text
    c = Fore.GREEN if color == 'verde' else Fore.RED
    print(c + text_output + Style.RESET_ALL)

class InfoBot(object):

    URL_INICIAL = 'https://www.infojobs.net'
    API_URL = 'https://api.infojobs.net/api'
    REQUEST_URL = 'https://developer.infojobs.net/test-console/execute.xhtml'

    def __init__(self, login_credentials=False):
        self.hello()
        if login_credentials:
            self.email = login_credentials['email']
            self.password = login_credentials['password']
            self.burp_proxy = login_credentials['burp']
        else:
            self.burp_config()
            self.ask_credentials()
        self.start()

    def hello(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        start_screen = """   ____     ___       _      __       ___       __ 
  /  _/__  / _/__    (_)__  / /  ___ / _ )___  / /_
 _/ // _ \/ _/ _ \  / / _ \/ _ \(_-</ _  / _ \/ __/
/___/_//_/_/ \___/_/ /\___/_.__/___/____/\___/\__/ 
                |___/                              """
        output(start_screen, 'verde', nostar=True)

    def ask_credentials(self):
        output(
            'Iniciando el bot, por favor introduce tus credenciales de acceso a infojobs',
            'verde'
        )
        output('Email:', 'verde')
        self.email = input()
        output('Password:', 'verde')
        self.password = getpass('')

    def burp_config(self):
        output('Estas usando Burp en 127.0.0.1:8080 [Y/N]', 'verde')
        user_answer = input()
        if user_answer != 'Y' and user_answer != 'N':
            output('Por favor responde solo con Y o N', 'r')
            self.burp_config()
        self.burp_proxy = True if user_answer == 'Y' else False

    def start(self):
        # Creamos sesion y si hace falta pasamos por burp
        self.session = requests.Session()
        if self.burp_proxy:
            proxies = {
                'http': 'http://127.0.0.1:8080',
                'https': 'http://127.0.0.1:8080'
            }
            self.session.proxies.update(proxies)

        # Saltamos barrera de distil
        try:
            jump_distil(self.session, self.URL_INICIAL)
            output('Sistema antibots neutralizado', 'verde')
        except:
            output(
                'Error saltando distil, engancha a burp y averigua el problema. \
                \nCerrando bot.',
                'r'
            )
            exit()

        # Hacemos login y pedimos permisos api
        try:
            info_login(self.email, self.password, self.session)
            output('Login y credenciales API ok!', 'verde')
        except:
            output(
                'Error haciendo login, engancha a burp y averigua el problema. \
                \nCerrando bot.',
                'r'
            )
            exit()

    def sleep(self):
        time.sleep(uniform(0.10, 1.5))

    def api_request(self, request_data, paginating=False):

        # Que haga las peticiones no tan uniformes
        self.sleep()

        response = self.session.post(
            self.REQUEST_URL,
            data=request_data,
            verify=False
        )
        if response.status_code != 200:
            output(
                f'Peticion a {request_data["urifield"]} fallida con status code \
                {response.status_code}, saliendo.'
            )
            exit()
        output(
            f'Peticion a {request_data["urifield"]} completada con exito',
            'verde'
        )

        # Sacamos el json
        soup = BeautifulSoup(response.text, 'html.parser')
        html_elem = soup.find(id='formattedBody')
        data = html_elem.string
        self.last_json = json.loads(data)

        if paginating:
            return self.last_json

        if 'currentPage' in self.last_json.keys():
            all_pages = []
            for n in range(1, self.last_json['totalPages']):
                if n == 1:
                    all_pages.append(self.last_json)
                else:
                    request_data['urifield'] = request_data['urifield'].replace(
                        '&page=' + str(n-1),
                        '&page=' + str(n)
                    )
                    response = self.api_request(request_data, paginating=True)
                    all_pages.append(response)
            return all_pages

        else:
            return self.last_json


    def list_offers(self, keyword, province=False):
        """
            Devuelve una lista con muchos json
            [{'currentPage':1,...}, {...}, ...]
        """
        url = self.API_URL + '/7/offer?q=' + keyword
        if province:
            url += '&province=' + province

        url += '&page=1'

        request_data = {
            'urifield': url,
            'methodfield': 'GET'
        }

        response = self.api_request(request_data)

        return response
        

def main():
    ib = InfoBot()
    ofertas_python = ib.list_offers('python')
    print(len(ofertas_python))

if __name__ == '__main__':
    main()
