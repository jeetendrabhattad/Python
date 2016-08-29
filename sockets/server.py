import socket
import sys
import threading

def SendRecv(connection, client_address):
    try:
        print('connection from, connection is', client_address, connection)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(10)
            print('received "%s"' % data)
            if data:
                print('sending data back to the client')
                connection.sendall(data)
            else:
                print("no more data from", client_address)
                break
    finally:
        # Clean up the connection
        connection.close()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10004)
print('starting up on %s port %s'%server_address)
sock.bind(server_address)
sock.listen(5)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    t1 = threading.Thread(target=SendRecv, args=(connection,client_address))
    t1.start()
