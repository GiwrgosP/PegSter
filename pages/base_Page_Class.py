from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class base_Page_Class(object):

    def __init__(self, driver):
        self.driver = driver

    def check_If_Element_Is_Present(self, element):
        try:
            wait = WebDriverWait(self.driver, 20)
            wait.until(EC.presence_of_element_located(element))
            return True
        except TimeoutException:
            print("Element is not located in the DOM ",element)
            return False

    def find_An_Element (self, element):

        if self.check_If_Element_Is_Present(element):
            return self.driver.find_element(*element)
        else:
            print("element not found ", element)
            return None

    def find_And_Click_An_Element(self, element):

        option = self.find_An_Element(element)

        if (option == None):
            return False
        else:
            option.click()
            print("clicked ", element)
            return True
