from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from infobot.bot import InfoBot
from bot.models import Offer



class Command(BaseCommand):

    def handle(self, *args, **options):

        # login = {
        #     'email': 'admin@victorciurana.com',
        #     'password': '',
        #     'burp': False
        # }

        # ib = InfoBot(login)
        ib = InfoBot()

        """
            Mete un monton de ofertas en la base de datos :D
            Mira si la oferta tiene preguntas y las guarda con respuestas
            para luego.
        """
        # python_offers = ib.list_offers('python')
        # for page in python_offers:
        #     for offer in page['offers']:
        #         try:
        #             Offer.objects.create(
        #                 _id = offer['id'],
        #                 title = offer['title'],
        #                 city = offer['city'],
        #                 link = offer['link'],
        #                 salaryDescription = offer['salaryDescription']
        #             )
        #         except IntegrityError:
        #             # Duplicado
        #             pass


        """
            Aplica a saco.
        """
        coverletter = {
            'coverLetter':{
                'name': 'test_name',
                'text': """Hola Soy Victor, y para demostrar mi habilidad como programador he decidido automatizar mi búsqueda de empleo. Ya que para mi un programador ha de ser capaz de automatizar todas las tareas aburridas y repetitivas, lo cual quiere decir que no tengo ni idea de a que estoy aplicando a parte de que dentro de la oferta aparece la palabra “Python”.

¿Es esto una buena idea?
Probablemente no, pero me he divertido un montón programando este robot y he aprendido varias cosas :)

¿Estoy buscando trabajo de verdad?
Sí, si tu empresa ofrece un trabajo donde no me aburra y se use python.

Puedes ver el siguiente vídeo donde explico cómo he creado el robot.
https://youtu.be/LnJGSKAgzN8

Que tenga un buen día.
"""
          }
        }
        n = 0
        for offer in Offer.objects.all():
            if not offer.applied:
                try:
                    ib.offer_application(offer._id, coverletter)
                    offer.applied = True
                    offer.response_text = ib.last_json
                    offer.save()
                except:
                    print('ERROR %s' % str(n))
                    n += 1

        print('EOF')
