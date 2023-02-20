import time
import datetime
from socket import *

#Step 1: Create a socket and bind it to the local host IP address
proxy_socket=socket(AF_INET,SOCK_STREAM)
proxy_socket.bind((gethostname(),10000))

#Step 2: capacity to listen
proxy_socket.listen(1) 
print ("The server can now receive")

while True:
    #Step 3: server acceptance of the connection and client's request
    connect, alpha = proxy_socket.accept()
    request = connect.recv(2048).decode() #from bytes to a string
    #Step 4: IP address extraction
    IP=request.split('/')[2]
    print("Connection from: ", alpha)
    print("Request sent at: ", IP,"Time", time.time())
    
    try:
        #Step 5: create a new socket & connect it to the final destination
        receiver_port = 80
        receiver_socket = socket(AF_INET,SOCK_STREAM)
        final_address = (IP, receiver_port)
        receiver_socket.connect(final_address) #connects the proxy Door
        receiver_socket.send(request.encode()) #send request to destination server
        
        print("Request sent at:",time.time())
        response = receiver_socket.recv(2048).decode() #receive response from the destination server  
        
        print("Request received at:",time.time())
        connect.send(response.encode()) #message sent from proxy to initial client
        print("Response sent back to client at:", time.time())
        receiver_socket.close()
        
    except:
        print("Error")
        connect.send("Something went wrong, repeat the process".encode())
    connect.close()