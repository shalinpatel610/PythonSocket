import socketserver


class MyTCPSocketHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """
    dict = {}
    
    def load_data(self):
        with open("data.txt") as f:
            lines = f.readlines()
        f.close()
        for line in lines:
            line = line.strip('\n')
            splits = line.split("|")
            key = splits[0]
            splits.pop(0)
            self.dict[key] = splits

    def handle(self):
        self.load_data()
        while True:
            data = self.request.recv(1024).decode("utf-8").strip()
            if not data:
                break
            print("Client Request : " + data)
            data = data.split("|")
            option = data[0]
            if option == '1':
                if data[1].strip() in self.dict:
                    send_list = [i.strip(" ") for i in self.dict[data[1]]]
                    send_str = data[1] + '|' + '|'.join(send_list)
                    self.request.sendall(bytes(send_str, "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            if option == '2':
                if data[1] in self.dict:
                    self.request.sendall(bytes("Customer already exist", "utf-8"))
                else:
                    input_list = [data[2], data[3], data[4]]
                    self.dict[data[1]] = input_list
                    self.request.sendall(bytes("Customer added successfully", "utf-8"))
            elif option == '3':
                if data[1].strip() in self.dict:
                    self.dict.pop(data[1])
                    self.request.sendall(bytes("Customer deleted successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '4':
                if data[1].strip() in self.dict:
                    input_list = self.dict[data[1]]
                    input_list[0] = data[2]
                    self.dict[data[1]] = input_list
                    self.request.sendall(bytes("Customer age updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '5':
                if data[1].strip() in self.dict:
                    input_list = self.dict[data[1]]
                    input_list[1] = data[2]
                    self.dict[data[1]] = input_list
                    self.request.sendall(bytes("Customer address updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '6':
                if data[1].strip() in self.dict:
                    input_list = self.dict[data[1]]
                    input_list[2] = data[2]
                    self.dict[data[1]] = input_list
                    self.request.sendall(bytes("Customer phone number updated successfully", "utf-8"))
                else:
                    self.request.sendall(bytes("Customer not found.", "utf-8"))
            elif option == '7':
                clean_d = {}
                for k, v in self.dict.items():
                    send_list = [i.strip(" ") for i in self.dict[k]]
                    clean_d[k] = send_list
                input_list = str(dict(sorted(clean_d.items())))
                self.request.sendall(bytes(input_list, "utf-8"))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    with socketserver.TCPServer((HOST, PORT), MyTCPSocketHandler) as server:
        server.serve_forever()
