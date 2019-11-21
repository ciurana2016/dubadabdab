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
    la huella pasarla los campos true y false bien

'''

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
    path = 'https://www.infojobs.net' + path
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

    info('Huella digital generada')
    return huella_digital

def main():
    s = requests.Session()
    # Provisional, pasar por Burp, o para debug
    proxies = {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
    s.proxies.update(proxies)

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
    huella_digital = generar_huella_digital()
    # Actualizamos headers
    headers_00['X-Distil-Ajax'] = ajax_header
    # Datos para POST
    post_data = {'p': str(huella_digital).replace("'",'"')}
    # Enviamos la peticion
    r = s.post(url_02, headers=headers_00, data=post_data, verify=False)
    xuid = r.headers['X-UID']

    # Ultimo get manual ?
    url_03 = 'https://www.infojobs.net/distil_identify_cookie.html?httpReferrer=/api/oauth/user-authorize/index.xhtml?scope=CANDIDATE_PROFILE_WITH_EMAIL&client_id=devsite-test-console-net&redirect_uri=https://developer.infojobs.net/test-console/continue-request.xhtml&response_type=code&state=CANDIDATE_PROFILE_WITH_EMAIL'
    url_03 += '&uid=' + xuid
    r = s.get(url_03, headers=headers_00, verify=False)


# MAIN SHIT
if __name__ == '__main__':
    info('Starting')
    main()
    info('EOF')
