from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_generate_a_new_short_url(self) -> None:
        TEST_LINK = 'https://www.neti.ee/'

        # He needs to dictate the link to a news story over the phone. He googles
        # for a link shortener and navigates to the page.
        self.browser.get('http://localhost:8000')

        # He notices that the page title and header mention that it is a URL
        # shortening service.
        self.assertIn('URLShortener', self.browser.title)

        # He sees a form there

        form = self.browser.find_element_by_tag_name('form').tag_name

        self.assertEqual(form, 'form')

        # He sees an input there and its label

        input_field = self.browser.find_element_by_tag_name('input').tag_name
        input_field_label = self.browser.find_element_by_tag_name('label').tag_name

        self.assertEqual(input_field, 'input')
        self.assertEqual(input_field_label, 'label')

        # He sees a submit button there

        button = self.browser.find_element_by_tag_name('button').tag_name
        button_content = self.browser.find_element_by_tag_name('button').text

        self.assertEqual(button, 'button')
        self.assertEqual(button_content, 'Send')

        # He is invited to paste in a link and click a button
        input_box = self.browser.find_element_by_id('link-generator-input')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Insert a link you want to shorten.')

        # He pastes in a link and clicks on a button
        input_box.send_keys(TEST_LINK)

        # When he hits Enter he is redirected to a new page.
        input_box.send_keys(Keys.ENTER)
        time.sleep(2)

        # He sees the title of the page
        self.assertIn('Your Link', self.browser.title)

        # He notices the original link and the generated link
        original_link = self.browser.find_element_by_id('original-link').text
        generated_link = self.browser.find_element_by_id('shortened-link').text
        print(original_link, generated_link)

        # He sees that the original link is the same one he entered into the form
        self.assertEqual(TEST_LINK, original_link)

        # He copies it and then visits it to check it.
        self.browser.get(generated_link)
        generated_title = self.browser.title
        self.browser.get(original_link)
        original_title = self.browser.title

        self.assertEqual(generated_title, original_title)

        # He is happy with the service provided and closes the browser.
