
class Server:
    def __init__(self, server_id, last_name, first_name):
        self._server_id = server_id
        self._last_name = last_name
        self._first_name = first_name

    def set_server_id(self, server_id):
        self._server_id = server_id

    def get_server_id(self):
        return self._server_id

    def set_last_name(self, last_name):
        self._last_name = last_name

    def get_last_name(self):
        return self._last_name

    def set_first_name(self, first_name):
        self._first_name = first_name

    def get_first_name(self):
        return self._first_name
