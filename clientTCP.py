from socket import *

serverName='127.0.0.1'
serverPort=12000
clientSocket=socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence=input("Enter the filename: ")

clientSocket.send(sentence.encode())
filecontents=clientSocket.recv(1024).decode()
print("Response from server:")
print(filecontents)