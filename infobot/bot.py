import os
import requests

from output import output
from getpass import getpass

from login import info_login
from distil import jump_distil




class InfoBot(object):

    URL_INICIAL = 'https://www.infojobs.net'

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


def main():
    ib = InfoBot()
    # Buscar trabajos

if __name__ == '__main__':
    main()
