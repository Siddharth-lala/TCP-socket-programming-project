import socket
import threading
import sys
import os

#Wait for incoming data from server
#.decode is used to turn the message in bytes to a string
def receive(socket, signal):
    while signal:
        try:
            data = socket.recv(32)
            newData = str(data.decode("utf-8"))
            if(newData == 'exit'):
                 
                break
                
            else:    
                print("\n"+newData)
            
        except:
            print("You have been disconnected from the server")
            signal = False
            sys.exit()

#Get host and port
host = "localhost"
port = 6666

#Attempt connection to server
try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((host, port))
    print("Connected to Server.....\n")
except:
    print("Could not make a connection to the server")
    input("Press enter to quit")
    sys.exit(0)

#Create new thread to wait for data
receiveThread = threading.Thread(target = receive, args = (sock, True))
receiveThread.start()

#Send data to server
#str.encode is used to turn the string message into bytes so it can be sent across the network
while True:
    message = input()
    if(message == 'exit'):
        break
    sock.sendall(str.encode(message))
    
    
