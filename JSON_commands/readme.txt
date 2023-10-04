Any changes inside the Json files would require an addition to the Zeus.py file, inside the menus and sub menus commands


        list_of_commands = ["show", "configure","edit"]
        list_show_subcommands = ["routing","compare","set"]
        list_edit_subcommands = ["class-of-service ","routing"]
        list_configure_subcommands = ["batch","exclusive","private"]

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