class Table_Creation_Menu:

    def __init__(self, restaurant):
        self._restaurant_object = restaurant

    def get_menu_configuration(self):
        return [
            {
                "option": "Create Table",
                "function": self.add_table_menu
            },
            {
                "option": "Edit Table",
                "function": self.update_table_menu
            },
            {
                "option": "Delete Table",
                "function": self.remove_table_menu
            },
            {
                "option": "Exit",
                "function": None
            }
        ]


    def add_table_menu(self):
        number_of_guest = 0
        table_id = 0

        menuMessage = "Please enter table ID: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        menuMessage = "Please enter number of guests:"
        userInput = input(menuMessage)
        number_of_guest = int(userInput)

        self._restaurant_object.add_table(table_id, number_of_guest)

    def update_table_menu(self):
        number_of_guest = 0
        table_id = 0

        menuMessage = "Please enter table ID to update: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        menuMessage = "Please enter number of guests:"
        userInput = input(menuMessage)
        number_of_guest = int(userInput)

        self._restaurant_object.update_table(table_id, number_of_guest)

    def remove_table_menu(self):
        number_of_guest = 0
        table_id = 0

        menuMessage = "Please enter table ID to remove: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        self._restaurant_object.delete_table(table_id)



"""
restaurant = Restaurant()
userMenu = Table_Creation_Menu(restaurant)
userMenu.menu();

"""