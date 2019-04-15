from django.test import TestCase
from LinkGenerator.forms import LinkGeneratorForm


class LinkGeneratorFormTest(TestCase):

    def test_form_renders_item_text_input_has_placeholder_and_css_classes(self):
        form = LinkGeneratorForm()

        self.assertIn('placeholder="Insert a link you want to shorten"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = LinkGeneratorForm(data={'text': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['original_link'],
            ['This field is required.']
        )