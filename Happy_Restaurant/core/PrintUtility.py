
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

def print_menu_items(menu_category):

    for category in menu_category.keys():
        print(category + ": ")
        #print individual item
        for single_item in menu_category[category]:
            print("\t%d. %s ($%.2f)" % (single_item.get_item_id(), single_item.get_item_name(), single_item.get_item_price()))

def split_check(order):
    print("Split check")

def single_check(order):
    print("Split check")
