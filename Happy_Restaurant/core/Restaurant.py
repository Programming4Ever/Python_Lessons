
from Table import Table

class Restaurant:

    def __init__(self):
        self._map_of_tables = {}
        self._list_of_orders = []

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

    def delete_table(self, table_id):
        self._map_of_tables[table_id] = None

    def seat_guests(self, order, total_guest):

        #Retrieve table ID
        table_id = order.get_table_id()

        #Retrieve table from the dictionary
        currentTable = self._map_of_tables.get(table_id)

        if(currentTable == None):
            return False

        #Check number of Guests to be <= table's seats
        if(total_guest > currentTable.get_guest_number()):
            return False

        #Is the table available?
        if(currentTable.get_status()):
            self._list_of_orders.append(order)
            currentTable.set_status(False)
            return True
        else:
            return False