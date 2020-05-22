import socket

HOST, PORT = "localhost", 9999


def send_data(value):
    sock.sendall(bytes(value, "utf-8"))
    received = str(sock.recv(1024), "utf-8")
    print("Sent:     {}".format(value))
    if value == '7':
        print("Received: \n")
        d = eval(received)
        print("{:<20} {:<5} {:<30} {:<10}".format('Name', 'Age', 'Address', 'Phone Number'))
        for key, value in d.items():
            x, y, z = value
            print("{:<20} {:<5} {:<30} {:<10}".format(key, x, y, z))
    else:
        print("Received: {}".format(received))


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
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

        if val == '1':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            send_data("1|" + name)
        if val == '2':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            while True:
                try:
                    age = input("Enter age: ")
                    if not age:
                        age = ""
                        break
                    else:
                        age = int(age)
                except ValueError:
                    print("Enter age in digits only!")
                    continue
                else:
                    break
            address = input("Enter address: ")
            phone = input("Enter phone number: ")
            send_data("2|" + name + "|" + str(age) + "|" + address + "|" + phone)
        if val == '3':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            send_data(("3|" + name))
        if val == '4':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            while True:
                try:
                    age = input("Enter age: ")
                    if not age:
                        age = ""
                        break
                    else:
                        age = int(age)
                except ValueError:
                    print("Enter age in digits only!")
                    continue
                else:
                    break
            send_data("4|" + name + "|" + str(age))
        if val == '5':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            address = input("Enter address: ")
            send_data("5|" + name + "|" + address)
        if val == '6':
            name = input("Enter name: ")
            while not name:
                name = input("Enter name: ")
            phone = input("Enter phone number: ")
            send_data("6|" + name + "|" + phone)
        if val == '7':
            send_data("7")
        elif val == '8':
            print("Good Bye!")
            sock.close()
            keepOn = False
        else:
            continue
