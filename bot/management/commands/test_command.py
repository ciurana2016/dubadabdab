from django.core.management.base import BaseCommand, CommandError

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
        # python_offers = ib.list_offers('python')
        # for page in python_offers:
        #     for offer in page['offers']:
        #         Offer.objects.create(
        #             _id = offer['id'],
        #             title = offer['title'],
        #             city = offer['city'],
        #             link = offer['link'],
        #             salaryDescription = offer['salaryDescription']
        #         )

        """
            Aplica a una oferta con una carta especifica.
            TODO, models offer si aplica y da error guardarlo.
        """
        