import os
import socketserver


class HealthLevel(object):
    DOWN = "down\n"
    UP = "up\n"
    MAINTENANCE = "maint\n"
    READY = "ready\n"


class HealthCheckHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        health_level = os.environ.get("FLASK_HEALTH_LEVEL", HealthLevel.READY)
        print("current health level: {}".format(health_level))
        self.request.sendall(bytes(health_level))


if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 8080

    # Create the server, binding to localhost on port 8080
    print("Start TCP Server...")
    with socketserver.TCPServer((HOST, PORT), HealthCheckHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
