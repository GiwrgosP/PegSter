from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class driver_Handler():

    default_Url = "https://george.pegcloud.io/pegasus_cloud_app/peg002_app/index.html"

    chrome_Options = Options()
    chrome_Options.add_experimental_option("detach", True)
    chrome_Options.add_argument("--disable-search-engine-choice-screen")
    chrome_Options.add_argument(f"--window-size=1366,768")

    fire_Fox_Options = Options()

    def __init__(self, browser):

        browser_Drivers = {
            "firefox" : lambda fire_Fox_Options = self.fire_Fox_Options : fire_Fox_Driver(options = fire_Fox_Options),\
            "chrome" : lambda chrome_Options = self.chrome_Options: webdriver.Chrome(options=chrome_Options)
                        }

        self.driver = browser_Drivers[browser]()
        self.driver.get(self.default_Url)

        self.driver.implicitly_wait(10)

class chrome_Driver(webdriver.Chrome):
    def __init__(self, options):
        super().__init__(options = options)

class fire_Fox_Driver(webdriver.Firefox):
    def __init__(self, options):
        super().__init__(options = options)
