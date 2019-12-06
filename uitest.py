from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import unittest

# to run these tests, first start the website using python manage.py runserver and then run this using python uitest.py

# uses the python unittest framework

class TestUI(unittest.TestCase):

    def test_website_title(self):

        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/')
        assert 'Rotten Potatoes' in browser.title
        browser.quit()

    def test_user_not_logged_in(self):

        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/logout')

        result = browser.find_element_by_xpath("//a[@class='sign_up' and text()='Sign in with Google']")

        assert result
        browser.quit()

    def test_user_settings_buttons_not_on_profile_when_not_logged_in(self):

        browser = webdriver.Chrome()
        browser.get('http://localhost:8000/users/bjcahill') #an example user

        settings_button_present = True
        logout_button_present = True

        try:
            settings_button = browser.find_element_by_xpath("//a[@class='mybtn' and text()='Go to Settings']")
        except:
            settings_button_present = False
        try:
            logout_button = browser.find_element_by_xpath("//a[@class='gobackcenter' and text()='Log out']")
        except:
            logout_button_present = False

        assert not settings_button_present
        assert not logout_button_present

        browser.quit()

if __name__ == '__main__':
    unittest.main()