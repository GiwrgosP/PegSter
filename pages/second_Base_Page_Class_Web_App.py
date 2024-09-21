from utils.locators import main_Navigation_Options_Base_Class as nav_Class
from pages.base_Page_Class import base_Page_Class

#gia to navigation
class second_Base_Page_Class(base_Page_Class):
    locators = nav_Class
    navi_Gate_Options_Available = {\
                                    "main_Screen_Top_Tool_Bar_Doc_Item" : {#einai i mpara me tis epiloges gia Epiloges,Dashboard, Anafores ktlp\
                                                                            "status_Active" : False,\
                                                                            "path" : locators.main_Screen_Top_Tool_Bar_Doc_Item\
                                                                        },\
                                    "peg_Tab_Bar" : {#einai i mple mpara me tis karteles gia kathe diaforetiki othoni tis efarmogis\
                                                    "status_Active" : False,\
                                                    "path" : locators.peg_Tab_Bar,\
                                                    },\
                                    "tool_Box_Button" : {\
                                                        "status_Active" : False,\
                                                        "path" : locators.tool_Box_Button\
                                                    }\
                                    }

    def __init__(self,driver):
        base_Page_Class.__init__(self,driver)

        for option in self.navi_Gate_Options_Available:
            self.navi_Gate_Options_Available[option]["status_Active"] = self.check_If_Element_Is_Present(self.navi_Gate_Options_Available[option]["path"])


    def navi_Gate_To_Instructions_Tool_Box(self,instructions):

        if self.navi_Gate_Options_Available["tool_Box_Button"]["status_Active"]:

            self.find_And_Click_An_Element(self.navi_Gate_Options_Available["tool_Box_Button"]["path"])

            current_Option_Level = nav_Class.tool_Box_Options
            for option in instructions:
                if option in current_Option_Level:
                    if self.find_And_Click_An_Element(current_Option_Level[option]["path"]):
                        if "sub_Options" in current_Option_Level[option]:
                            current_Option_Level = current_Option_Level[option]["sub_Options"]
                        else:
                            print(f"No sub-options for {option}")
                            return
                    else:
                        print(f"{option} could not be clicked")
                        return
                else:
                    print(f"{option} was not found in the current option level")

    def navi_Gate_To_Instructions_Actions(self,instructions):

        actions_Menu_Button, actions_Sub_Option_Button = instructions

        if actions_Menu_Button in object_Class.actions_Menu_Buttons_List:

            if action in object_Class.actions_Menu_Buttons_List[actions_Menu_Button]["sub_Options"]:
                self.find_And_Click_An_Element(object_Class.actions_Menu_Buttons_List[actions_Menu_Button]["sub_Options"][actions_Sub_Option_Button]["path"])
