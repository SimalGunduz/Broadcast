import socket 
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

server.settimeout(0.2)
server.bind(('255.255.255.255' ,21922 ))
message = b'Your very important message'

while True:
    server.sendto(message, ('<broadcast>',7777 ))
    print("Message sent!")
time.sleep(1)