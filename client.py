import socket

HOST, PORT = "localhost", 9998


def sendData(val):
    sock.sendall(bytes(val, "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(val))
    if val == '7':
        print("Received: \n")
        d = eval(received)
        print("{:<15} {:<5} {:<20} {:<10}".format('Name', 'Age', 'Address', 'Phone Number'))
        for name, value in d.items():
            age, address, phone = value
            print("{:<15} {:<5} {:<20} {:<10}".format(name, age, address, phone))
    else:
        print("Received: {}".format(received))

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    sock.connect((HOST, PORT))
    keepOn = True

    while keepOn:
        print("\nDB OPTIONS\n")
        print("1. Find  customer")
        print("2. Add customer")
        print("3. Delete customer")
        print("4. Update customer age")
        print("5. Update customer address")
        print("6. Update customer phone number")
        print("7. Print report")
        print("8. Exit\n")
        val = input("Select: ")
        print(val)

        if val == '1':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            sendData("1|" + name)
        if val == '2':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            age = input("Enter age: ")
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            sendData("2|" + name + "|" + age + "|" + address + "|" + phone)
        if val == '3':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            sendData(("3|" + name))
        if val == '4':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            age = input("Enter age: ")
            while not age:
                age = input("Enter age: ")
            sendData("4|" + name + "|" + age)
        if val == '5':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            address = input("Enter address: ")
            while not address:
                age = input("Enter address: ")
            sendData("5|" + name + "|" + address)
        if val == '6':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            phone = input("Enter phone number: ")
            while not age:
                phone = input("Enter phone number: ")
            sendData("6|" + name + "|" + phone)
        if val == '7':
            sendData("7")
        elif val == '8':
            print("Good Bye!")
            keepOn = False
        else:
            print("Please enter a number.")

