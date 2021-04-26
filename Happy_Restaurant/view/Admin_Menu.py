
from core.PrintUtility import *
from dao.External_Configuration import *

class AdminMenu:

    def __init__(self, restaurant):
        self._restaurant_object = restaurant

    def get_menu_configuration(self):
        return [
            {
                "option": "Table Status",
                "function": self.print_table_status
            },
            {
                "option": "Print Tips",
                "function": None
            },
            {
                "option": "Print Menu",
                "function": self.print_menu_items
            },
            {
                "option": "Load Configurations",
                "function": self.load_configurations
            },
            {
                "option": "Save Configurations",
                "function": self.save_configurations
            }
        ]

    # This function print table statuses
    def print_table_status(self):
        table_status(self._restaurant_object.get_table_as_list())

    # This function print table statuses
    def print_menu_items(self):
        print_menu_items(self._restaurant_object.get_menu_by_category())

    # This function save configurations
    def save_configurations(self):
        save_table_configuration(self._restaurant_object.get_table_as_list())

    # This function load configuration
    def load_configurations(self):
        #Load table configurations
        self._restaurant_object.load_table_map(load_table_configuration())

        #Load Menu
        self._restaurant_object.load_menu_item_map(load_menu_configuration())

        #Load Server Data
        self._restaurant_object.load_server_data(load_server_configuration())
