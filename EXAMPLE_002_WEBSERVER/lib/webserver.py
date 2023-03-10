class Webserver:

    def __init__(self, ip_address, port, socket):
        self.connection = None
        self.ipAddress = ip_address
        self.port = port
        self.socket = socket

    def open_socket(self):
        print("listening for requests")
        # Open a socket
        address = (self.ipAddress, self.port)
        socket = self.socket.socket()
        socket.bind(address)
        socket.listen(1)
        self.connection = socket
        return socket

    def serve(self, connection):
        while True:
            self.serve_client(connection)

    def serve_client(self, connection):
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        client.send('{"id": "blah"}')
        client.close()
