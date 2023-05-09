from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from local.models import LocalItem
from local.views import details
import requests

API_TEMPLATE = "http://discovery.nationalarchives.gov.uk/API/records/v1/details/{id}"

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument("itemid")
    
    def handle(self, *args, **options):

        if 'itemid' not in options:
            raise TypeError("Missing positional argument :itemid: in call to cacheitem command.")
        
        item = None

        try:
            item = LocalItem.objects.get(pk=options['itemid'])
            self.stdout.write("Item exists locally: using cached version")
        except LocalItem.DoesNotExist:
            response = requests.get(API_TEMPLATE.format(id=options['itemid']))

            if response.status_code == 200:
                architem = response.json()

                item = LocalItem.objects.create(
                    arch_id=architem['id'],
                    title=architem['title'],
                    description=architem['scopeContent']['description'],
                    reference=architem['citableReference']
                )

        view = details(None, options['itemid'])

        self.stdout.write(view.content.decode())