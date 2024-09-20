from selenium.webdriver.common.by import By

class login_Page_For_Web_App (object):
    #Not Used+++++++++++++++++++++++++++++++++++
    language_Drop_Down_List = 'C1_lang-trigger-picker'
    language_Input = 'C1_lang-inputEl'
    theme_Drop_Down_List = 'C1_theme-trigger-picker'
    theme_Input = 'C1_theme-inputEl'
    #Not Used+++++++++++++++++++++++++++++++++++

    user_Name_Field = (By.ID, 'C1_p800-inputEl')
    pass_Word_Field = (By.ID, 'C1_p801-inputEl')
    submit_Button = (By.ID, 'C1_login-btnInnerEl')

    wrong_Pass_Word_Message_Box = (By.ID, 'messagebox-1017')
    wrong_Pass_Word_Message_Box_Button = (By.ID, 'button-1021-btnInnerEl')

class main_Accordion (object):
    main_Accordion_Body = (By.ID, '_main_d_accordion-body')

    #estiasi
    estiasi_Main_Panel = (By.ID, 'panel-1067_header')
    estiasi_Reception_Button = (By.ID, 'pegasusAccordionItemShow_d-1068-btnEl')
    estiasi_Kratiseis_Button = (By.ID, 'pegasusAccordionItemBrowse-1069-btnEl')

    #......
    #Pelates
    customers_Main_Panel = (By.ID, 'panel-1157_header')
    customers_Retail_Button = (By.ID, 'pegasusAccordionItemAction-1158-btnEl')

    customers_Invoices_Button = (By.ID, 'pegasusAccordionItemBrowse-1160-btnEl')


#sto panw meros emfanizontai buttons gia epiloges, anafores, xristi ktlp
#nomizw oti einai kali idea gia ena geniko nativation class (den kserw an tha einai idio gia mobile)
class main_Navigation_Options_Base_Class(object):

    main_Screen_Top_Tool_Bar_Doc_Item = (By.ID, '_main_d_screen_docitem_top-innerCt')
    main_Screen_Peg_Tab_Bar = (By.ID, 'peg__main_d_tabbar-innerCt')

    #prepei na kanw kai ta upoloipa
    tool_Box_Button = (By.ID, '_main_d_toolbarbutton_140000000000204-btnIconEl')

    tool_Box_Options =\
    {\
    "Βάσεις Δεδομένων" : {\
                        "path" : (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/table[1]/tbody/tr/td/div"),\
                        "sub_Options" : {\
                                        "Πελάτες" : {\
                                                    "path" : (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/table[15]/tbody/tr/td/div"),\
                                                    "sub_Options" : {\
                                                                    "Παραστατικά Πελατών" : {\
                                                                                            "path": (By.XPATH, "/html/body/div[1]/div[2]/div/div/div[3]/div/div[2]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[2]/table[18]/tbody/tr/td/div")\
                                                                                            }
                                                                    }
                                                    }
                                        }
                        }
    }

class customers_Invoices_List_Class(main_Navigation_Options_Base_Class):

    main_Screen_Top_Tool_Bar = (By.ID, 'pegasusToolBar-1416-innerCt')

    quick_Find_Button = (By.ID, 'C21_grid_quickfindbutton')
    quick_Find_Help = (By.ID, 'C21_grid_quickfindhelp')

    actions_Menu_Buttons_List = \
    {\
    "Ενέργειες" : {\
                    "path" : (By.ID, 'C21_menu_grid_top'),
                    "sub_Options" : {\
                                    "Νέα Καταχώρηση(Ins)" : (By.ID, 'C21_grid_toolbaritem_insert-itemE'),
                                    "Διαχείριση" : (By.ID, 'C21_grid_toolbaritem_edit-itemEl'),
                                    "Αντιγραφή" : (By.ID, 'C21_grid_toolbaritem_copy-itemEl'),
                                    "Διαγραφή" : (By.ID, 'C21_grid_toolbaritem_delete-itemEl'),
                                    "Καθαρισμός Φίλτρων" : (By.ID, 'C21_grid_toolbaritem__clearfilters-itemEl')
                                    }
                  }
    }


    #c21_Menu_Tool_Bar_Item_Search = (By.ID, 'C21_grid_toolbaritem_search-itemEl')


    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
    #c21_Menu_Tool_Bar_Item_Insert = (By.ID, 'C21_grid_toolbaritem_insert-itemE')
