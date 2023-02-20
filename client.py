import socket
import time
import uuid
# serverName is the local host
serverName= '127.0.0.1'
serverPort=8888
# define the website
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
#send the request to the proxy server
message=input("eneter the ip address")
#send the request to the proxy server
clientSocket.sendall(message.encode())
beginTime=time.time()
#receieve the response from the proxy server
response= clientSocket.recv(1024).decode()
print(f" the response is:{response}")
endTime=time.time()
totalTime= endTime-beginTime
print(f"the total round trip time is:{totalTime}")
# display and calculat the MAC address of the host and to get the MAC address you use function uuid 
print ("The MAC address in formatted way is : ", end="") 
print (':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff)
for ele in range(0,8*6,8)][::-1]))
clientSocket.close()

 