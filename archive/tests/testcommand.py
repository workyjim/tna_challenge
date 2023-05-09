from django.test import TestCase
from io import StringIO
from django.core.management import call_command

KNOWN_IDS = [
    {
        "id": "N13759454",
        "output": "minute books, cash book, accounts, registers of payments and beneficiaries"
    },
    {
        "id": "a147aa58-38c5-45fb-a340-4a348efa01e6",
        "output": "<p>Titan Tractor</p>"
    }
]

class CommandTests(TestCase):

    def test_known_ids(self):
        for item in KNOWN_IDS:
            out = StringIO()
            call_command("cacheitem", item['id'], stdout=out)
            self.assertEquals(out.getvalue().strip(), item['output'].strip())
    
    def test_unknown_ids(self):
        out = StringIO()
        call_command("cacheitem", "definitely-invalid-item-id", stdout=out)
        self.assertEquals(out.getvalue().strip(), "no record found")

    def test_ids_already_cached(self):
        for item in KNOWN_IDS:
            # cache the item once to ensure it's in the test db
            call_command("cacheitem", item['id'])
            
            out = StringIO()
            call_command("cacheitem", item['id'], stdout=out)
            self.assertEquals(out.getvalue().strip(), "Item exists locally: using cached version\n{detail}".format(detail=item['output'].strip()))


