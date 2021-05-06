from core.Table import Table
from core.MenuItem import MenuItem
from core.Server import Server
import json
from util.TimeUtil import *

"""
    This function is for saving table configurations.
"""


def save_table_configuration(table_list):
    data_list = []
    for singleTable in table_list:
        data_list.append(singleTable.__dict__)
    output_file = open("storage/tables.json", "w")
    json.dump(data_list, output_file)
    output_file.close()


# This function is for loading table configurations.
def load_table_configuration():
    table_map = {}
    input_file = open("storage/tables.json")
    json_data = json.load(input_file)
    input_file.close()
    for single_table in json_data:
        table_map[single_table["_table_id"]] = Table(single_table["_table_id"], single_table["_guest_number"])

    # Return a map of all tables
    return table_map


# This function is for loading food menu configurations.
def load_menu_configuration():
    food_map = {}
    input_file = open("storage/food_menu.json")
    json_data = json.load(input_file)
    input_file.close()
    for menu_item in json_data:
        food_map[menu_item["_item_id"]] = MenuItem(menu_item["_item_id"], menu_item["_item_name"],
                                                   menu_item["_category"], menu_item["_item_price"])

    # Return a map of all tables
    return food_map

# This function is for loading server information
def load_server_configuration():
    server_map = {}
    input_file = open("storage/server_data.json")
    json_data = json.load(input_file)
    input_file.close()
    for server in json_data:
        server_map[server["_server_id"]] = Server(server["_server_id"], server["_last_name"], server["_first_name"])

    # Return a map of all server data
    return server_map

# The goal for this function is to save order data.  It will append to the given file by day
def save_order_information(order):
    # Get today date to create file format
    file_name = "storage/order_" + get_today_date() + ".json"
    output_file = open(file_name, "a")
    json.dump(order, output_file)
    output_file.write("\n")
    output_file.close()

def print_tip_data(server_data_list):
    for single_server in server_data_list:
        print( "%s\t%.2f\n" % (single_server["Name"], single_server["Tip"]))