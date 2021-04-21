import datetime
from MenuItem import MenuItem

class Order:
    def __init__(self, table_number, server_id, number_of_guest):
        self._table_number = table_number
        self._server_id = server_id
        self._number_of_guest = number_of_guest

        #All built in object attributes.  We do not need them
        self._order_id = None   #Auto generated
        self._guest_orders = {}
            # Guest Orders: Dictionary
            # {Guest Number, List of Menu Items}
        self._service_fee = .15     #percent for tips
        self._tax = .1  # 10% tax
        self._date = None

    def get_table_id(self):
        return self._table_number

    def get_server_id(self):
        return self._server_id

    def get_guest_orders(self):
        return self._guest_orders

    def add_guest_order(self, guestNumber, order):
        orderList = self._guest_orders.get(guestNumber)
        #Guest has not ordered anything
        if (orderList == None):
            orderList = [order]
            self._guest_orders[guestNumber] = orderList
        else:
            orderList.append(order)

    #Calculate sub-total for the order
    def calculate_subtotal(self):
        subtotal = 0.0
        for key in self._guest_orders.keys() :
            for singleItem in self._guest_orders.get(key):
                subtotal += singleItem.get_item_price()
        return subtotal

    # Calculate service fee for the order
    def calculate_service_fee(self):
        return self.calculate_subtotal() * self._service_fee

    # Calculate tax
    def calculate_tax(self):
        return self.calculate_subtotal() * self._tax

    # Calculate Total
    def calculate_total(self):
        return self.calculate_subtotal() + self.calculate_service_fee() + self.calculate_tax()

