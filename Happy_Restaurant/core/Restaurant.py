
from core.Table import Table

class Restaurant:

    def __init__(self):
        self._map_of_tables = {}
        self._list_of_orders = []
        self._food_menu = {}
        self._menu_by_group = {}
        self._server_map = {}

    def get_table_as_list(self):
        list_of_table = []
        for key in self._map_of_tables.keys():
            list_of_table.append(self._map_of_tables.get(key))
        return list_of_table

    def add_table(self, table_id, number_of_guest):
        self._map_of_tables[table_id] = (Table(table_id, number_of_guest))

    def update_table(self, table_id, number_of_guest):
        singleTable = self._map_of_tables.get(table_id)

        #Does the table exist
        if (singleTable != None):
            #update only when table exists
            singleTable.set_guest_number(number_of_guest)

    #This function is loading table data
    def load_table_map(self, table_map):
        self._map_of_tables = table_map

    #This function is loading server data
    def load_server_data(self, server_map):
        self._server_map = server_map

    # This function is loading menu items
    def load_menu_item_map(self, food_menu):
        self._food_menu = food_menu

        #Create menu by group
        for single_key in food_menu.keys():
            single_item = food_menu.get(single_key)
            category_list = self._menu_by_group.get(single_item.get_category())
            if category_list == None:
                category_list = []
                self._menu_by_group[single_item.get_category()] = category_list

            #Add data to the list
            category_list.append(single_item)

    def get_menu_by_category(self):
        return self._menu_by_group

    def delete_table(self, table_id):
        self._map_of_tables[table_id] = None

    def seat_guests(self, order):
        #Retrieve table ID
        table_id = order.get_table_id()

        #Retrieve table from the dictionary
        currentTable = self._map_of_tables.get(table_id)

        if(currentTable == None):
            raise Exception("Table Does Not Exist!")

        #Check number of Guests to be <= table's seats
        if(order.get_number_of_guests() > currentTable.get_guest_number()):
            raise Exception("Table has less seats than number of guests!")

        #Is the table available?
        if(currentTable.get_status()):
            self._list_of_orders.append(order)
            currentTable.set_status(False)
            return True
        else:
            raise Exception("Table is not available!")