import pytest

class loginToWebApp(selenium):
        def __init__(self,url):
            self.driver = webdriver.Firefox()
            self.url = url

        def accessUrl(self):
            self.driver.get(self.url)

        def login_to_Pegasus_Web_App(self):

            self.accessUrl()

            login_page = LoginPageWebApp(self.driver)

            login_page.loginToWebAppFunction()
