from core.Table import Table
import json

"""
    This class contains all save and load functionalities the Restaurant
"""

class DataRepository:

    def save_table_configuration(self, tableList):
        dataList = []
        for singleTable in tableList:
            dataList.append(singleTable.__dict__)
        outputFile = open("../tables.json", "w")
        json.dump(dataList, outputFile)
        outputFile.close()

    def load_table_configuration(self):
        tableList = []
        inputFile = open("../tables.json", "w")
        jsonData = json.load(inputFile)
        inputFile.close()
        for singleTable in jsonData:
            tableList.append(Table(singleTable._table_id, singleTable._guest_number))

        #Return a list of all tables
        return tableList