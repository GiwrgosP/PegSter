from utils.locators import login_Page_For_Web_App
from pages.base_Page_Class import base_Page_Class


from selenium.webdriver.common.keys import Keys

class login_Page_Web_App(base_Page_Class):

    user_Credencials = {"admin" : {"username" : "admin", "password" : "HummingBiurd2!"}}

    def __del__(self):
        print("deleted login_class")

    def __init__(self,driver):
        base_Page_Class.__init__(self,driver)

        self.locators = login_Page_For_Web_App


        self.user_Name_Field = self.find_An_Element(self.locators.user_Name_Field)
        self.pass_Word_Field = self.find_An_Element(self.locators.pass_Word_Field)
        self.submit_Button = self.find_An_Element(self.locators.submit_Button)

    def set_User_Credencials(self,user):

        self.user_Name_Field.send_keys(self.user_Credencials[user]["username"])
        self.pass_Word_Field.send_keys(self.user_Credencials[user]["password"])

    def login_To_Web_App_Function(self):

        self.submit_Button.click()
        wrong_Pass_Word_Message_Box = self.check_If_Element_Is_Present(self.locators.wrong_Pass_Word_Message_Box)

        if (wrong_Pass_Word_Message_Box):

            wrong_Pass_Word_Message_Box_Button = self.find_An_Element(self.locators.wrong_Pass_Word_Message_Box_Button)
            wrong_Pass_Word_Message_Box_Button.click()

            self.submit_Button.click()

            wrong_Pass_Word_Message_Box = self.check_If_Element_Is_Present(self.locators.wrong_Pass_Word_Message_Box)

            if (wrong_Pass_Word_Message_Box):
                print("Wrong Credencials for login")
            else:
                print("Login with second try")
