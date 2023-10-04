import tkinter
from tkinter import *
from tkinter import ttk

import customtkinter
import webbrowser

from tkterminal import Terminal
import sys

from scripts import beorn_collector, navigator, logic

########### from tkterminal import Terminal 
#####For later

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")

# Logger
import logging

logging.basicConfig(
    filename="./logs/zeus.log",
    level=logging.DEBUG,
    format="%(module)s : %(levelname)s:  %(message)s - : %(asctime)s",
)


class App(customtkinter.CTk,tkinter.Tk):
    def __init__(self):
        super().__init__()

        sub_menu_option=None
        # configure window
        self.title("Zeus")
        self.geometry(f"{1400}x{600}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure((3, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        ############# Left Grid
        ######## create sidebar frame with widgets left side
        self.sidebar_frame = customtkinter.CTkFrame(self, width=50, corner_radius=25)
        self.sidebar_frame.grid_rowconfigure(8, weight=10)
        self.sidebar_frame.grid(row=0, column=0, padx=20, pady=10, sticky="ewns")

        self.logo_label = customtkinter.CTkLabel(
            self.sidebar_frame,
            text="ZEUS",
            font=customtkinter.CTkFont(size=40, weight="bold"),
        )
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        ##### Top Left Buttons
        self.sidebar_button_2 = customtkinter.CTkButton(
            self.sidebar_frame, text="BEORN", command=self.sidebar_button_2
        )
        self.sidebar_button_2.grid(row=3, column=0, padx=20, pady=(20, 10))


        self.sidebar_button_3 = customtkinter.CTkButton(
            self.sidebar_frame, text="MDSO", command=self.sidebar_button_3
        )
        self.sidebar_button_3.grid(row=4, column=0, padx=20, pady=(20, 10))


        self.sidebar_button_4 = customtkinter.CTkButton(
            self.sidebar_frame, text="Snippit", command=self.sidebar_button_4
        )
        self.sidebar_button_4.grid(row=5, column=0, padx=20, pady=(20, 70))


        ##### Bottom Left
        ## scaling and color theme
        self.appearance_mode_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="Appearance Mode:", anchor="w"
        )
        self.appearance_mode_label.grid(row=9, column=0, padx=20, pady=10)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(
            self.sidebar_frame,
            values=["Light", "Dark"],
            command=self.change_appearance_mode_event,
        )
        self.appearance_mode_optionemenu.grid(row=10, column=0, padx=20, pady=(0, 0))

        self.scaling_label = customtkinter.CTkLabel(
            self.sidebar_frame, text="UI Scaling:", anchor="w"
        )
        self.scaling_label.grid(row=11, column=0, padx=20, pady=20)

        # self.scaling_optionemenu = customtkinter.CTkOptionMenu(
        #     self.sidebar_frame,
        #     values=["80%", "90%", "100%", "110%", "120%", "150%"],
        #     command=self.change_scaling_event,
        # )
        # self.scaling_optionemenu.grid(row=12, column=0, padx=20, pady=(0, 20))

        self.scaling_slider = customtkinter.CTkSlider(self.sidebar_frame,from_=80,to=110,command=self.change_scaling_event)
        self.scaling_slider.configure(number_of_steps = 5)
        self.scaling_slider.grid(row=12, column=0, padx=20, pady=(0, 20))

        ########### Right Grid
        ######## Labels and thier correspondant Box
        self.tabview = customtkinter.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=2, padx=10, pady=10, sticky="new")
        self.tabview.configure(width = 1000,height=650)
        # Devices Tabs
        self.tabview.add("IP Address")
        self.tabview.add("Junipor")
        self.tabview.add("ADVA")
        self.tabview.add("RAD")

        ###### Output Boxes 

        self.address_output_textbox = customtkinter.CTkTextbox(
            self.tabview.tab("IP Address"), height=500, corner_radius=25
        )

        self.juni_output_textbox = customtkinter.CTkTextbox(self.tabview.tab("Junipor"), corner_radius=25
        )
        self.juni_output_textbox.grid(row=0, column=1, padx=10, pady=(50,10), sticky="new")
        self.juni_output_textbox.configure(wrap="word",width= 850,height=450 ,font=("non-Serif", 20))

        self.address_output_textbox.grid(row=0, column=1, padx=10, pady=(50,10), sticky="new")
        self.address_output_textbox.configure(wrap="word",width= 850,height=450 ,font=("non-Serif", 20))

        self.adva_output_textbox = customtkinter.CTkTextbox(
            self.tabview.tab("ADVA"), corner_radius=25
        )
        self.adva_output_textbox.grid(row=0, column=1, padx=10, pady=(50,10), sticky="new")
        self.adva_output_textbox.configure(wrap="word",width= 850,height=450 ,font=("non-Serif", 20))

        self.rad_output_textbox = customtkinter.CTkTextbox(
            self.tabview.tab("RAD"),  height=450,corner_radius=25
        )
        self.rad_output_textbox.grid(row=0, column=1, padx=10, pady=(50,10), sticky="new")
        self.rad_output_textbox.configure(wrap="word",width= 850,height=450 ,font=("non-Serif", 20))




        ######### Middle Grid
        self.tabview = customtkinter.CTkTabview(self, corner_radius=25)
        self.tabview.grid(row=0, column=1, padx=1, pady=10, sticky="nw")
        self.tabview.configure(height=950)
        # Beorn Tab
        self.tabview.add("Beorn")

        self.tabview.tab("Beorn").grid_columnconfigure(
            0, weight=10
        )
        
        ######## Incoming Arguments
        self.CID_Entry = customtkinter.CTkEntry(
            self.tabview.tab("Beorn"), placeholder_text="CID", width=175
        )
        self.CID_Entry.grid(row=2, column=0, padx=55, pady=10)

        ################
        # Future use to take the argument and use it to log in 
        # example ssh 000.000.000.000 -l username 
        ################
        self.username_entry = customtkinter.CTkEntry(
            self.tabview.tab("Beorn"), placeholder_text="MDSO username", width=175
        )
        self.username_entry.grid(row=3, column=0, padx=55, pady=10)

        #################################
        #################################
        # this block here was hard to be moved anywhere else reason is
        # it inherit TTK and not Custkinter the functionality of having submenus 
        # so it had to exist before the drop down menus
        # to be inherant instead of menus and embeded sub menus
        #################################
        #################################
        list_of_commands = ["show", "configure","edit"]
        list_show_subcommands = ["routing","compare","set"]
        list_edit_subcommands = ["class-of-service ","routing"]
        list_configure_subcommands = ["batch","exclusive","private"]
        sub_menu_value = None
        def pick_submenu (e):
            if self.main_command.get() == "show":
                self.Sub_command.config(value=list_show_subcommands)
                sub_menu_value = self.Sub_command.get()
                return sub_menu_value

            if self.main_command.get() == "edit":
                self.Sub_command.config(value=list_edit_subcommands)
                sub_menu_value = self.Sub_command.get()
                return sub_menu_value
                
            if self.main_command.get() == "configure":
                self.Sub_command.config(value=list_configure_subcommands)
                sub_menu_value = self.Sub_command.get()
                return sub_menu_value
        
        ########### Drop down boxes for command and sub command
        self.main_command = ttk.Combobox(self.tabview.tab("Beorn"),values=list_of_commands)

        self.main_command.grid(row=4, column=0, padx=55, pady=10)
        ####bind the combobox with a fucntion that triggers the sub commands
        self.main_command.bind("<<ComboboxSelected>>",pick_submenu)
        
        self.Sub_command = ttk.Combobox(self.tabview.tab("Beorn"),values=[""])
        self.Sub_command.grid(row=5, column=0, padx=55, pady=10)

        ########### Middle Grid Button / s
        self.devices_button = customtkinter.CTkButton(
            self.tabview.tab("Beorn"),
            text="Devices",
            command=self.Devices_button
        )
        self.devices_button.grid(row=7, column=0, padx=75, pady=(150, 50))



#################################
#################################
#### Functions
#################################
#################################

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        # print(float)
        new_scaling_float = int(new_scaling) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    # def slider_event(self):
    #     pass

    ############# middle Grid Button function
    ### connects and triggers the beorn collector .py 
    # done this way because each function here couldn't connect to a button, or CTK Entry without a function outside the __init__ function 
    def Beorn_topologies_button_functionality(self):
        beorn_collector.beorn_api_caller(self)
        return

    def Devices_button(self):
        logic.device_sorter(self)
        return



    ############### Left side Buttons 
    ##### Connects to Navigator.py inside scripts
    def sidebar_button_2(self):
        navigator.leftside_beorn_butt(self)
    def sidebar_button_3(self):
        navigator.leftside_MDSO_butt(self)
    def sidebar_button_4(self):
        navigator.snippit_button(self)

if __name__ == "__main__":
    app = App()
    app.mainloop()
