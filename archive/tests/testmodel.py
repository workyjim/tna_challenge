from local.models import LocalItem
from django.test import TestCase

class ModelTests(TestCase):
    _id = "test-item-1"
    _title = "The test item's title"
    _description = "The test item's scopeContent.description"
    _reference = "The test item's citableReference"
    
    def test_str(self):
        item = LocalItem(arch_id=self._id, title=self._title, description=self._description, reference=self._reference)
        self.assertEqual(str(item), self._title)

    def test_title_null(self):
        item = LocalItem(arch_id=self._id, description=self._description, reference=self._reference)
        self.assertEqual(str(item), self._description)

    def test_title_scdesc_null(self):
        item = LocalItem(arch_id=self._id, reference=self._reference)
        self.assertEqual(str(item), self._reference)

    def test_title_scdesc_ref_null(self):
        item = LocalItem(arch_id=self._id)
        self.assertEqual(str(item), "not sufficient information")

