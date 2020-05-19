import socketserver


class MyTCPSocketHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    dict = {}
    def loadData(self):
        with open("data.txt") as f:
            lines = f.readlines()
        f.close()
        for l in lines:
            l = l.strip('\n')
            splits = l.split("|")
            key = splits[0]
            splits.pop(0)
            self.dict[key] = splits

    def handle(self):
        self.loadData()
        while True:
            data = self.request.recv(1024).decode("utf-8").strip()
            if not data:
                break
            print(data)
            data = data.split("|")
            option = data[0]
            if option == '1':
                if data[1].strip() in self.dict:
                    sendStr = data[1] + '|' + '|'.join(self.dict[data[1]])
                    self.request.sendall(bytes(sendStr, "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            if option == '2':
                l = []
                l.append(data[2])
                l.append(data[3])
                l.append(data[4])
                self.dict[data[1]] = l
                self.request.sendall(bytes("Customer added successfully", "utf-8"))
            elif option == '3':
                if data[1].strip() in self.dict:
                    self.dict.pop(data[1])
                    self.request.sendall(bytes("Customer deleted successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '4':
                if data[1].strip() in self.dict:
                    l = self.dict[data[1]]
                    l[0] = data[2]
                    self.dict[data[1]] = l
                    self.request.sendall(bytes("Customer age updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '5':
                if data[1].strip() in self.dict:
                    l = self.dict[data[1]]
                    l[1] = data[2]
                    self.dict[data[1]] = l
                    self.request.sendall(bytes("Customer address updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '6':
                if data[1].strip() in self.dict:
                    l = self.dict[data[1]]
                    l[2] = data[2]
                    self.dict[data[1]] = l
                    self.request.sendall(bytes("Customer phone number updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '7':
                l = str(dict(sorted(self.dict.items())))
                self.request.sendall(bytes(l, "utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9998

    # instantiate the server, and bind to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()
