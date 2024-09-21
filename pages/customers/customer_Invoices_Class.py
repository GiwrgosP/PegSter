from pages.second_Base_Page_Class_Web_App import second_Base_Page_Class
from utils.locators import customers_Invoices_List_Class


class customer_Invoices_Class(second_Base_Page_Class):

    navi_Gate_Instructions_Tool_Box = ("Βάσεις Δεδομένων","Πελάτες","Παραστατικά Πελατών")

    locators = customers_Invoices_List_Class

    def __init__(self,driver,instructions):
        second_Base_Page_Class.__init__(self,driver)

        self.navi_Gate_To_Instructions_Tool_Box(self.navi_Gate_Instructions_Tool_Box)
