from django.core.management.base import BaseCommand, CommandError
from django.db import IntegrityError

from infobot.bot import InfoBot
from bot.models import Offer



class Command(BaseCommand):

    def handle(self, *args, **options):

        login = {
            'email': 'admin@victorciurana.com',
            'password': '',
            'burp': False
        }

        ib = InfoBot(login)

        """            Mete un monton de ofertas en la base de datos :D
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
            Aplica a una oferta con una carta especifica.
            TODO, guardar response entera
            TODO for o in offers apply with letter
        """
        