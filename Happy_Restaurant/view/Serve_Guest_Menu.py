from core.Order import Order

class Serve_Guest_Menu:

    def __init__(self, restaurant):
        self._restaurant_object = restaurant

    def get_menu_configuration(self):
        return [
            {
                "option": "Seat Guests",
                "function": self.seat_guest
            },
            {
                "option": "Take Order",
                "function": None
            },
            {
                "option": "Checkout",
                "function": None
            },
            {
                "option": "Exit",
                "function": None
            }
        ]


    def seat_guest(self):
        number_of_guest = 0
        table_id = 0
        server_id = 0

        menuMessage = "Please enter server ID:"
        userInput = input(menuMessage)
        server_id = int(userInput)

        menuMessage = "Please enter table ID: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        menuMessage = "Please enter number of guests:"
        userInput = input(menuMessage)
        number_of_guest = int(userInput)

        newOrder = Order(table_id, server_id)

        self._restaurant_object.seat_guests(newOrder, number_of_guest)
        print("New object created")



"""
restaurant = Restaurant()
userMenu = Table_Creation_Menu(restaurant)
userMenu.menu();

"""