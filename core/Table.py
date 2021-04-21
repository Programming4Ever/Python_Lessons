
class Table:
    def __init__(self, table_id, guest_number):
        self._table_id = table_id
        self._guest_number = guest_number
        self._status = True

    def set_table_id(self, table_id):
        self._table_id = table_id

    def get_table_id(self):
        return self._table_id

    def set_guest_number(self, guest_number):
        self._guest_number = guest_number

    def get_guest_number(self):
        return self._guest_number

    def set_status(self, status):
        self._status = status

    def get_status(self):
        return self._status


