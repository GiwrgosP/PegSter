from pages.second_Base_Page_Class import second_Base_Page_Class


class customer_Invoices_Class(second_Base_Page_Class):
    def __init__(self,driver,instructions):
        second_Base_Page_Class.__init__(self,driver)

        get_To_Page_Instructions = ("Βάσεις Δεδομένων","Πελάτες","Παραστατικά Πελατών")
