
from core.Table import Table
from dao.External_Configuration import *

class Restaurant:

    def __init__(self):
        self._map_of_tables = {}
        self._map_of_orders = {}
        self._food_menu = {}
        self._menu_by_group = {}
        self._server_map = {}
        self._server_tips = {}

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

        #Initialize Server Tips
        for server_id in server_map.keys():
            self._server_tips[server_id] = 0.00


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

    #This function creates order data
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
            self._map_of_orders[table_id] = order
            currentTable.set_status(False)
            return True
        else:
            raise Exception("Table is not available!")

    def get_order_data(self, order):
        order_data = {}
        order_data["Table Number"] = order.get_table_id()
        order_data["Order Date"] = order._date
        order_data["Order ID"] = order._order_id

        service_fee_total = tax_total = sub_total = total = 0.00


        guest_list = []
        order_data["Guest List"] = guest_list

        for guest_number in order.get_guest_orders().keys():

            #Guest Data
            guest_orders = {}

            #Add to list
            guest_list.append(guest_orders)

            # Convert to Guest Order
            guest_orders["Guest Number"] = guest_number

            guest_order_data = order.get_guest_orders()
            guest_order_list = guest_order_data.get(guest_number)

            order_item_list = []
            guest_orders[guest_number] = order_item_list

            # Print out orders per guest
            for single_item in guest_order_list:
                order_item = {}
                order_item["Name"] = single_item.get_item_name()
                order_item["price"] = single_item.get_item_price()
                order_item_list.append(order_item)

                service_fee_total = service_fee_total + order.calculate_service_fee_by_guest(guest_number)
                tax_total = tax_total + order.calculate_tax_by_guest(guest_number)
                sub_total = sub_total + order.calculate_subtotal_by_guest(guest_number)
                total = total + order.calculate_total_by_guest(guest_number)

        # Print Order data
        guest_orders["Service Fee"] = service_fee_total
        guest_orders["Tax:"] = tax_total
        guest_orders["Sub-Total"] = sub_total
        guest_orders["Total"] = total

        return order_data

    #This function check out the guests
    def checkout_guest(self, table_id):

        #Retrieve table from the dictionary
        currentTable = self._map_of_tables.get(table_id)

        if(currentTable == None):
            raise Exception("Table Does Not Exist!")

        #Set table to be available
        currentTable.set_status(True)

        #Retrieve Order Data
        current_order = self._map_of_orders[table_id]

        #Persist data
        save_order_information( self.get_order_data(current_order) )

        #Store order tips data
        self._server_tips[current_order.get_server_id()] = self._server_tips[current_order.get_server_id()] \
                                                           + current_order.calculate_service_fee()

        #Delete unused data
        del self._map_of_orders[table_id]

    def get_server_tips_info(self):
        server_list = []
        for server_id in self._server_tips:
            server_data = self._server_map[server_id]
            info_map = {}
            server_list.append(info_map)
            info_map["Name"] = server_data.get_first_name() + " " + server_data.get_last_name()
            info_map["Tip"] = self._server_tips[server_id]

        return server_list

    #This function retrieves order data based on table ID
    def get_order_by_table(self, table_id):
        return self._map_of_orders.get(table_id)

    #This function adds food for a specific guest to a specific table
    def add_order(self, table_id, guest_id, food_id):

        order = self._map_of_orders.get(table_id)
        if order is None:
            raise Exception("No Order Found for Table");

        single_food_item = self._food_menu.get(food_id);
        if single_food_item is None:
            raise Exception("No Food Found")

        order.add_guest_order(guest_id, single_food_item)

    #This function returns all current orders
    def get_all_current_orders(self):
        list_of_table = []
        for key in self._map_of_orders.keys():
            list_of_table.append(self._map_of_orders.get(key))
        return list_of_table
