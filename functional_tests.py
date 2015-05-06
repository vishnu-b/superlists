from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Manoharan has heard about a cool new online to-do app.
        # He goes to check out it's homepage
        self.browser.get('http://localhost:8000')

        # He notices the page title and header mention To-Do Lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish test')

        # He is invited to enter a to-do item straight away

        # He enters "Get some good mechanics" into the textbox.
        # (Manoharan runs K & K Automobiles)

        # When he hits enter the page updates. Now the page lists
        # "1. Get some good mechanics" as an item in to-do list

        # There is still a textbox inviting him to enter another to-do item.
        # He enters "Get a contract from M N Nambiar" (M N Nambiar owns
        # so many caaars)

        # The page updates again and now it shows both items on the to-do list

        # Manoharan wonders whether the site will be able to remember his
        # list. Then he notices the site has generated a unique URL for him
        # -- there is some explanatory text to that effect

        # He visits that URL - his to-do list is still there

if __name__ == '__main__':
    unittest.main()
