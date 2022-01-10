from socket import *
serverName="127.0.0.1"
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(1)
while 1:
    print ("The server is ready to receive")
    connectionSocket, addr = serverSocket.accept()
    # print(connectionSocket,addr)
    sentence = connectionSocket.recv(1024).decode()
    print(sentence)
    l=""
    try:
        file=open(sentence,"r")
        l=file.read(1024)
        file.close()
    except FileNotFoundError:
        l="File Not found"
    # print(str(file))
    connectionSocket.send(l.encode())
    print ("Sent contents of " + sentence)
    
    connectionSocket.close()
    exit(0)
