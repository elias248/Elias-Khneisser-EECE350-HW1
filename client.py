from socket import*
import time
import uuid

#Step 1: create a TCP socket
client_socket=socket(AF_INET,SOCK_STREAM)
#connect client socket to the proxy server running at port 10000
client_socket.connect((gethostname(),10000)) 
#IP address of the server they want to connect
IP = input("Enter IP address:")
#Step 2: Create an HTTP request string to send to the server
request = "Get http://" + IP + "/ HTTP/1.0\n\n"
#Step 3: Send request to the server & convert the request string to bytes
client_socket.send(request.encode())
req_time = time.time()
print("Message sent is:", request, "Sent at:", time.time())
#receive response from server & convert the bytes to a string.
response = client_socket.recv(2048).decode()

resp_time = time.time()
#Step 4: calculate the round-trip time
RTT = resp_time - req_time
print ("Response from server:", response, "at time:", time.time())
print ("The process took:", RTT)
print ("Mac address is:", hex(uuid.getnode()))
