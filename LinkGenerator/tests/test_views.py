from django.test import TestCase
from LinkGenerator.forms import LinkGeneratorForm


class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'LinkGenerator/index.html')

    def test_home_uses_link_generator_form(self):
        response = self.client.get('/')

        self.assertIsInstance(response.context['form'], LinkGeneratorForm)