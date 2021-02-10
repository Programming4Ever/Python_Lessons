
class Server:
    def __init__(self):
        self._serverName = ""
        self._serverId = ""

    def set_serverName(self, serverName):
        self._serverName = serverName

    def set_serverName(self, serverName):
        self._serverName = serverName

    def set_serverId(self, serverId):
        self._serverId = serverId

    def get_serverName(self):
        return self._serverName

    def get_serverId(self):
        return self._serverId

    def print(self):
        print("Server Name = %s.  Server ID = %s " % (self._serverName, self._serverId))

newServer = Server()
newServer.set_serverName("Eric (Test)")
newServer.set_serverId("1")
newServer.print()


newServer2 = Server()
newServer2.set_serverName("Daphne")
newServer2.set_serverId("2")
newServer2.print()

