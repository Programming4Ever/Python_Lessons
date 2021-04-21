from core.Restaurant import Restaurant
from view.Table_Creation_Menu import Table_Creation_Menu
from core.PrintUtility import PrintUtility
from dao.External_Configuration import DataRepository
from view.Serve_Guest_Menu import Serve_Guest_Menu
import datetime


#This is where the program will start

def startInput(template):
    # print out options
    menuMessage = ""
    menuIndex = 1;
    for singleOption in template:
        menuMessage = menuMessage + (("%d. " + singleOption["option"] + "\n") % (menuIndex))
        menuIndex = menuIndex + 1

    user_input = 0
    while (True):
        user_input = input(menuMessage)
        try:
            user_input = int(user_input)

            if (user_input > 0 and user_input <= len(template)):
                break
            else:
                print("Please only input data from the given options.")
        except:
            print("Invalid Input:  Please only input data from the given options.")

    # Retrieve values from the option
    option = template[user_input - 1]

    # Retrieve function
    targetFunction = option["function"]

    if (targetFunction != None):
        targetFunction()

print(int(datetime.datetime.now().strftime("%Y%m%d%H%M%S")))
#Create Restaurant
restaurant = Restaurant()

#Create User Menu for Table
userMenu = Table_Creation_Menu(restaurant)

serve_guest_menu = Serve_Guest_Menu(restaurant)

#This object will be used for loading/saving data
storeData = DataRepository()

#Create Main Menu
main_menu = """1. Table Creation Menu
2. Serve Guest Menu
3. Admin Menu
4. Exit Program
"""

#start program

while(True):

    menu_input = input(main_menu)

    if(menu_input == "1"):
        startInput(userMenu.get_menu_configuration())
        printer = PrintUtility()
        printer.table_status(restaurant.get_table_as_list())
        storeData.save_table_configuration(restaurant.get_table_as_list())
    elif (menu_input == "2"):
        startInput(serve_guest_menu.get_menu_configuration())
    elif (menu_input == "3"):
        print("Admin Menu\n")
    elif (menu_input == "4"):
        print("Have a great day!\n")
        break
    else:
        print("Please choose one of the 3 options.\n")

"""

userMenu.menu()




printer = PrintUtility()
printer.table_status(restaurant.get_table_as_list())





table1 = Table(1, 3, 1)
table2 = Table(2, 3, 1)
table3 = Table(3, 3, 0)
listOfTables = [table1, table2, table3]

printUtil = PrintUtility()

printUtil.table_status(listOfTables)

print(table1.__dict__)

testMenu = MenuItem(1, "Test Name", "Group", 300)
testMenu2 = MenuItem(2, "Test Name", "Group", 100)
testOrder = Order(1, testMenu)

testOrder.add_guest_order(1,testMenu)
testOrder.add_guest_order(1,testMenu2)
testOrder.add_guest_order(5,testMenu2)

print("Order Sub-Total = %f " % (testOrder.calculate_subtotal() ) )
print("Service Fee = %f " % (testOrder.calculate_service_fee() ) )
print("Tax = %f " % (testOrder.calculate_tax() ) )

print("Total = %f " % (testOrder.calculate_total() ) )


outputFile = open("myJason.json", "w")
json.dump(restaurant.get_table_as_list2(), outputFile)
"""