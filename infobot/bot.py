# -*- coding: utf-8 -*-

import os
import json
import time
import requests

from output import output
from random import uniform
from getpass import getpass
from bs4 import BeautifulSoup

from login import info_login
from distil import jump_distil




class InfoBot(object):

    URL_INICIAL = 'https://www.infojobs.net'
    API_URL = 'https://api.infojobs.net/api'
    REQUEST_URL = 'https://developer.infojobs.net/test-console/execute.xhtml'

    def __init__(self):
        self.hello()
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
