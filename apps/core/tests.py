from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class TestViews(TestCase):
    def test_index_page_works(self):
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)