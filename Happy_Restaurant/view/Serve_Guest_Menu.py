from core.Order import Order
from core.PrintUtility import *

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
                "function": self.take_order
            },
            {
                "option": "Checkout",
                "function": self.check_out
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

        newOrder = Order(table_id, server_id, number_of_guest)

        try:
            self._restaurant_object.seat_guests(newOrder)
        except Exception as error_msg:
            print(error_msg)

    def take_order(self):
        number_of_guest = 0
        table_id = 0

        # Take table ID to get order Information
        menuMessage = "Please enter table ID: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        while True:
            menuMessage = "Enter x to exit.\nPlease enter Guest Number: "
            guest_number = input(menuMessage)
            if guest_number == 'x' or guest_number == 'X':
                break

            while True:
                menuMessage = "Enter x to exit.\nPlease Item Number: "
                food_id = input(menuMessage)
                if food_id == 'x' or food_id == 'X':
                    break
                #Add data
                self._restaurant_object.add_order(table_id, int(guest_number), int(food_id))

    def check_out(self):
        number_of_guest = 0
        table_id = 0

        # Take table ID to get order Information
        menuMessage = "Choose Receipt Type: \nPress 1 for Split-Check\nAnything else for Single-Check\n"
        receipt_type = input(menuMessage)

        menuMessage = "Please enter table ID: "
        userInput = input(menuMessage)
        table_id = int(userInput)

        #Retrieve Order to print out receipt
        single_order = self._restaurant_object.get_order_by_table(table_id)

        if receipt_type == '1':
            split_check(single_order)
        else:
            single_check(single_order)

        #call restaurant to check out
        self._restaurant_object.checkout_guest(table_id)