from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

PORT_NUMBER = 5001
SIZE = 1024

hostName = gethostbyname('0.0.0.0')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print ("Test server listening on port {0}\n".format(PORT_NUMBER))


def receive():
    (data, addr) = mySocket.recvfrom(SIZE)
    return data


def close():
    sys.ext()

# while True:
#         (data,addr) = mySocket.recvfrom(SIZE)
#         print data
# sys.ext()
