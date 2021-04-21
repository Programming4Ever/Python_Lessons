
from Table import Table

class PrintUtility:

    def available_table(self, listOfTables):
        for singleTable in listOfTables:
            if(singleTable.get_status() == 1):
                print("Table %d" % (singleTable.get_table_id()) )

    def unavailable_table(self, listOfTables):
        for singleTable in listOfTables:
            if(singleTable.get_status() == 0):
                print("Table %d" % (singleTable.get_table_id()) )

    def table_status(self, list_of_tables):
        for singleTable in list_of_tables:
                status = "Available"

                if(singleTable == None):
                    continue

                if(singleTable.get_status() == 0):
                    status = "Unavailable"
                print("Table %d ==> Status = %s" % (singleTable.get_table_id(), status))

    def split_check(self, order):
        print("Split check")

    def single_check(self, order):
        print("Split check")
