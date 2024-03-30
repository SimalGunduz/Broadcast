from socket import *
	#addr = ('192.168.0.255',10000) 
addr = ('<broadcast>',7777) 
		
s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1) 
s.bind(('255.255.255.255',7777))
while True:
    
	data,addr = s.recvfrom(1024)

	print("received message: %s"%data)
	acaddr=addr[0]
	acdata=data.decode()
	alldata={acdata:acaddr}
	for x,y in alldata.items():
		print(x,y)
	#s.close()
