from socket import *;

client=socket(AF_INET, SOCK_DGRAM)
sentence=input("Enter the file name: ")
client.sendto(sentence.encode("utf-8"),("127.0.0.1",12000))
contents,addr=client.recvfrom(2048)
print("Reply from server")
print(contents.decode("utf-8"))
print("Server Address:"+str(addr))