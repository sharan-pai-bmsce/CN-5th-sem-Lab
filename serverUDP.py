from socket import *;
server=socket(AF_INET, SOCK_DGRAM)
server.bind(("127.0.0.1",12000))
print("Server is ready")
while 1:
    sentence,addr=server.recvfrom(2048)
    sentence=sentence.decode("utf-8")
    file=open(sentence,'r')
    contents=file.read(2048)
    server.sendto(contents.encode('utf-8'),addr)
    print("Sent contents of "+sentence)
    file.close()
    exit(0)
