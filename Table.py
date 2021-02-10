
"""
Total number of seat
Current number of guest
Is this table available?
Who is serving this table


"""

class Table:

    def __init__(self, tableNumber):
        self._tableNumber = tableNumber
        self._numberOfSeat = 0
        self._currentNumberOfGuest = 0
        self._available = True
        self._serverId = None

    def set_tableNumber(self, tableNumber):
        self._tableNumber = tableNumber

    def set_currentNumberOfGuest(self, currentNumberOfGuest):
        if(currentNumberOfGuest < self._numberOfSeat):
            self._currentNumberOfGuest = currentNumberOfGuest
        else:
            print("Error")

    def set_numberOfSeat(self, numberOfSeat):
        self._numberOfSeat = numberOfSeat

    def set_available(self, available):
        self._available = available

    def set_serverId(self, serverId):
        self._serverId = serverId

    def get_tableNumber(self):
        return self._tableNumber

    def get_currentNumberOfGuest(self):
        return self._currentNumberOfGuest

    def get_numberOfSeat(self):
        return self._numberOfSeat

    def get_available(self):
        return self._available

    def get_serverId(self):
        return self._serverId
