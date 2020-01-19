from django.core.management.base import BaseCommand

from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

from scraping.models import TechModel

class Command(BaseCommand):
    help = "coletar matérias"

    def handle(self, *args, **options):

        #coletar htmls
        html = urlopen('https://www.tecmundo.com.br/')

        #converter para o formato soup
        soup = BeautifulSoup(html, 'html.parser')

        #obtendo todos os posts da classe tec--carousel__item__info
        notices = soup.find_all("div", class_="tec--carousel__item__info")

        for n in notices:
            title = n.find('h2').text

            try:
                TechModel.objects.create(
                    title=title
                )
                print("Matéria \"%s\" adicionada" ,% (title))
            except:
                print('May the title %s already exists' % (title))
        self.stdout.write('Notice completed')