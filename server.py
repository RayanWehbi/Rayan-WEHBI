import socket
import time
# Define the Serverport and address
serverName=""
serverPort =8888
# create a socket to listen for the connections and bind it to the serverPort
serverSocket = socket.socket (socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen()
print ("The server is ready to receive")
while True:
#Acceptence of the connection
#client socket 
    clientSocket, address = serverSocket.accept()# getting request from the client
    print(f"connection from {address}")
    request =clientSocket.recv(1024)
    print(f"the request is recieved from {request}")
    #define destination destination server IP address from the request and it t0 the destination server
    ipAddress= request
    request_message=f"GET / HTTP/1.1\r\nServerName:{ipAddress}\r\n\r\n"
    print(request_message)
    print(f"the destiation server ip address is:{ipAddress}")
    print(time.time())
    # create new socket to connect to server
    destinationSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    destinationSocket.connect((ipAddress,80))
    # the port number is 80 since we access http website
    #send the request of client to the destination server 
    destinationSocket.sendall(request.encode())
    print(f"the request is send to the address:{ipAddress}")
    print(time.time())
    #define and receive the response from the destination socket
    response= destinationSocket.recv(1024)
    print("The request is recieved")
    #send the response back to the client
    destinationSocket.sendall(response)
    print("The request is back to the client")
    print(time.time())
serverSocket.close()
destinationSocket.close()
    

