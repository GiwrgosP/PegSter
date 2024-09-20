
# import all required frameworks

from pages.login_Page_Class_Web_App import login_Page_Web_App
from pages.second_Base_Page_Class_Web_App import second_Base_Page_Class
from utils.selenium_Driver_Handler import driver_Handler

class PegSter_Tester_test(object):

    driver_H = driver_Handler("chrome")

    def __init__(self):
        self.driver = self.driver_H.driver

    def login_to_Pegasus_Web_App(self):
        self.test_Prepare = login_Page_Web_App(self.driver)
        self.test_Prepare.set_User_Credencials("admin")
        self.test_Prepare.login_To_Web_App_Function()

    def get_To_Some_Where (self):
        del self.test_Prepare

        self.test_Get_To_Some_Where = second_Base_Page_Class(self.driver)

def main():

    k = PegSter_Tester_test()
    k.login_to_Pegasus_Web_App()
    k.get_To_Some_Where()

# execute the script
if __name__ == "__main__":
    main()
