# Python program to implement server side of chat room.
import socket
import select
import sys
Port = 1999
IP_address = "192.168.1.84"
from _thread import start_new_thread


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# checks whether sufficient arguments have been provided
# if len(sys.argv) != 3:
#     print("Correct usage: script, IP address, port number")
#     exit()

# # takes the first argument from command prompt as IP address
# IP_address = str(sys.argv[1])

# # takes second argument from command prompt as port number
# Port = int(sys.argv[2])

print("Binding ...")
server.bind((IP_address, Port))

"""
listens for 100 active connections. This number can be
increased as per convenience.
"""
print("Listening")
server.listen(100)

list_of_clients = []


def clientthread(conn, addr):

    # sends a message to the client whose user object is conn
    conn.send(bytes("Welcome to this chatroom!", "utf-8"))

    message = conn.recv(2048)
    print(message)
    if message:

        """prints the message and address of the
        user who just sent the message on the server
        terminal"""
        message = str(message.decode("utf-8"))
        print("<" + addr[0] + "> " + message)

        # Calls broadcast function to send message to all
        message_to_send = "<" + addr[0] + "> " + str(message)
        broadcast(message_to_send, conn)

    else:
        """message may have no content if the connection
        is broken, in this case we remove the connection"""
        print("Connection lost")
        remove(conn)





def broadcast(message, connection):
    for clients in list_of_clients:
        if clients != connection:
            print(clients, "is not in list")
            try:
                print("Sending message")
                clients.send(bytes(message, "utf-8"))
            except:
                print("Error")





def remove(connection):
    print(connection in list_of_clients)
    if connection in list_of_clients:
        print("Removing client : ", connection)
        list_of_clients.remove(connection)


while True:


    conn, addr = server.accept()

    list_of_clients.append(conn)

    # prints the address of the user that just connected
    print(addr[0] + " connected")

    # creates and individual thread for every user
    # that connects
    start_new_thread(clientthread, (conn, addr))

conn.close()
server.close()
