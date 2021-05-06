from core.Restaurant import Restaurant
from view.Table_Creation_Menu import Table_Creation_Menu
from view.Serve_Guest_Menu import Serve_Guest_Menu
from view.Admin_Menu import AdminMenu


# This is where the program will start

def start_input(template):
    # print out options
    menu_message = ""
    menu_index = 1
    for singleOption in template:
        menu_message = menu_message + (("%d. " + singleOption["option"] + "\n") % (menu_index))
        menu_index = menu_index + 1

    user_input = 0
    while True:
        print("\n\n")
        user_input = input(menu_message)
        try:
            user_input = int(user_input)

            if 0 < user_input <= len(template):
                break
            else:
                print("Please only input data from the given options.")
        except Exception:
            print("Invalid Input:  Please only input data from the given options.")

    # Retrieve values from the option
    option = template[user_input - 1]

    # Retrieve function
    target_function = option["function"]

    if target_function is not None:
        target_function()


# Create Restaurant
restaurant = Restaurant()

# Create User Menu for Table
userMenu = Table_Creation_Menu(restaurant)

serve_guest_menu = Serve_Guest_Menu(restaurant)

admin_menu = AdminMenu(restaurant)
#Load data when the system loads
admin_menu.load_configurations()

# Create Main Menu
main_menu = """1. Table Creation Menu
2. Serve Guest Menu
3. Admin Menu
4. Exit Program
"""

# start program

while True:

    menu_input = input(main_menu)

    if menu_input == "1":
        start_input(userMenu.get_menu_configuration())
    elif menu_input == "2":
        start_input(serve_guest_menu.get_menu_configuration())
    elif menu_input == "3":
        start_input(admin_menu.get_menu_configuration())
    elif menu_input == "4":
        print("Have a great day!\n")
        break
    else:
        print("Please choose one of the 3 options.\n")
