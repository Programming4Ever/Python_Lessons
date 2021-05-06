
def available_table(listOfTables):
    for singleTable in listOfTables:
        if(singleTable.get_status() == 1):
            print("Table %d" % (singleTable.get_table_id()) )

def unavailable_table(listOfTables):
    for singleTable in listOfTables:
        if(singleTable.get_status() == 0):
            print("Table %d" % (singleTable.get_table_id()) )

def table_status(list_of_tables):

    if len(list_of_tables) == 0:
        print("No table to display.")
        return;

    for singleTable in list_of_tables:
            status = "Available"

            if(singleTable == None):
                continue

            if(singleTable.get_status() == 0):
                status = "Unavailable"
            print("Table %d ==> Status = %s" % (singleTable.get_table_id(), status))

    print("\n")

def print_table_and_orders(list_of_orders):

    if len(list_of_orders) == 0:
        print("No Order to display")
        return;

    for single_order in list_of_orders:
            print("Table Number %d" % (single_order.get_table_id()))

            for guest_number in single_order.get_guest_orders().keys():
                print("\tGuest Number: %d" % (guest_number))
                guest_order_data = single_order.get_guest_orders()
                guest_order_list = guest_order_data.get(guest_number)

                #Print out orders per guest
                for single_item in guest_order_list:
                    print("\t\t%s ($%.2f)" % (single_item.get_item_name(), single_item.get_item_price()))
    print("\n")

def print_menu_items(menu_category):

    for category in menu_category.keys():
        print(category + ": ")
        #print individual item
        for single_item in menu_category[category]:
            print("\t%d. %s ($%.2f)" % (single_item.get_item_id(), single_item.get_item_name(), single_item.get_item_price()))

def split_check(order):
    print("Table Number %d" % (order.get_table_id()))

    for guest_number in order.get_guest_orders().keys():
        print("Guest Number: %d" % (guest_number))
        guest_order_data = order.get_guest_orders()
        guest_order_list = guest_order_data.get(guest_number)

        # Print out orders per guest
        for single_item in guest_order_list:
            print("\t%s ($%.2f)" % (single_item.get_item_name(), single_item.get_item_price()))

        #Print Order data
        print("\t Service Fee: $%.2f" % (order.calculate_service_fee_by_guest(guest_number)))
        print("\t Tax: $%.2f" % (order.calculate_tax_by_guest(guest_number)))
        print("\t Sub-Total: $%.2f" % (order.calculate_subtotal_by_guest(guest_number)))
        print("\t Total: $%.2f" % (order.calculate_total_by_guest(guest_number)))
        print("\n")

def single_check(order):
    print("Table Number %d" % (order.get_table_id()))

    service_fee_total = tax_total = sub_total = total = 0.00
    for guest_number in order.get_guest_orders().keys():
        print("Guest Number: %d" % (guest_number))
        guest_order_data = order.get_guest_orders()
        guest_order_list = guest_order_data.get(guest_number)

        # Print out orders per guest
        for single_item in guest_order_list:
            print("\t%s ($%.2f)" % (single_item.get_item_name(), single_item.get_item_price()))

            service_fee_total = service_fee_total + order.calculate_service_fee_by_guest(guest_number)
            tax_total = tax_total + order.calculate_tax_by_guest(guest_number)
            sub_total = sub_total + order.calculate_subtotal_by_guest(guest_number)
            total = total +order.calculate_total_by_guest(guest_number)

    # Print Order data
    print("\t Service Fee: %.2f" % (service_fee_total))
    print("\t Tax: %.2f" % (tax_total))
    print("\t Sub-Total: %.2f" % (sub_total))
    print("\t Total: %.2f" % (total))
    print("\n")
