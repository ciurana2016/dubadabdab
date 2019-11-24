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
        python_offers = ib.list_offers('python')
        for page in python_offers:
            for offer in page['offers']:
                try:
                    Offer.objects.create(
                        _id = offer['id'],
                        title = offer['title'],
                        city = offer['city'],
                        link = offer['link'],
                        salaryDescription = offer['salaryDescription']
                    )
                except IntegrityError:
                    # Duplicado
                    pass

        """
            Aplica  aoferta especifica 
            Para testear respuesta automaticas a preguntas
            fe6a3f9e674c6abb7341e9a1f6ed7a
        """

        # offer_with_question = Offer.objects.get(_id='fe6a3f9e674c6abb7341e9a1f6ed7a')

        # coverletter = {
        #     'coverLetter':{
        #         'name': 'test_name',
        #         'text': 'Test automatizado con python, no responder.'
        #   }
        # }


        """
            Aplica a saco.
        """
        # coverletter = {
        #     'coverLetter':{
        #         'name': 'test_name',
        #         'text': 'Test automatizado con python, no responder.'
        #   }
        # }

        # for offer in Offer.objects.all()[::-1]:
        #     if not offer.applied:
        #         ib.offer_application(offer._id, coverletter)
        #         offer.applied = True
        #         offer.response_text = ib.last_json
        #         offer.save()
        #         break

        # print('EOF')
