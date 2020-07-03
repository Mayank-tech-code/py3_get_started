import socket

# create a socket object
# SOCK_STREAM = TCP socket, SOCK_DGRAM = UDP
# AF_INET = Type of address our socket can communitcate with (IPv4)
serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = "127.0.0.1"

port = 65432

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
   # establish a connection
   clientsocket,addr = serversocket.accept()

   print("Got a connection from %s" % str(addr))
   
   data = clientsocket.recv(1024)
   print(data)
    
   msg = 'Thank you for connecting'+ "\r\n"
   clientsocket.send(msg.encode('ascii'))
   clientsocket.close()
