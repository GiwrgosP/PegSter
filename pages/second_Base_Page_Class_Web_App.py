from utils.locators import main_Navigation_Options_Base_Class as nav_Class
from pages.base_Page_Class import base_Page_Class

#gia to navigation
class second_Base_Page_Class(base_Page_Class):

    def __init__(self,driver):
        base_Page_Class.__init__(self,driver)

        navi_Gation_Peg_Tab_Bar = self.check_If_Element_Is_Present(nav_Class.main_Screen_Peg_Tab_Bar)

        instructions = navi_Gate_To_Tool_Box_Options

        if (main_Screen_Top_Tool_Bar_doc):

            self.tool_Box = top_Tool_Bar_Doc_Item

            self.find_And_Click_An_Element(self.tool_Box.tool_Box_Button)
            self.navi_Gate_To_Instructions_Tool_Box(instructions)

        else:
            pass

    def chech_For_Top_Tool_Bar(self,instructions):

        main_Tool_Bar_Doc = self.check_If_Element_Is_Present(nav_Class.main_Screen_Top_Tool_Bar_Doc_Item)
        if main_Tool_Bar_Doc:
            tool_Bar_Button = self.check_If_Element_Is_Present(nav_Class.tool_Box_Button)
            if tool_Bar_Button:
                self.navi_Gate_To_Instructions_Tool_Box(instructions)

    def navi_Gate_To_Instructions_Tool_Box(self,instructions):

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

    def navi_Gate_To_Instructions_Actions(self,object_Class,instructions):

        actions_Menu_Button, actions_Sub_Option_Button = instructions

        if actions_Menu_Button in object_Class.actions_Menu_Buttons_List:

            if action in object_Class.actions_Menu_Buttons_List[actions_Menu_Button]["sub_Options"]:
                self.find_And_Click_An_Element(object_Class.actions_Menu_Buttons_List[actions_Menu_Button]["sub_Options"][actions_Sub_Option_Button]["path"])
