from local.views import details
from local.views import LocalItem
from django.test import TestCase
from django.http.response import HttpResponse

class ViewTests(TestCase):
    _id = "test-item-1"
    _title = "The test item's title"
    _description = "The test item's scopeContent.description"
    _reference = "The test item's citableReference"


    def setUp(self):
        LocalItem.objects.create(arch_id=self._id, title=self._title)

    def test_known_item_response(self):
        self.assertEquals(details(None, self._id).content, self._title.encode())
    
    def test_unknown_item_response(self):
        self.assertEqual(details(None, "invalid-item-id").content, 'no record found'.encode())