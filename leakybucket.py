import random
import time
def main():
    SIZE=int(input("enter the number of packets: "))
    pk=[]
    for i in range(0,SIZE):
        pk.append(random.randint(1,100))
        print("packet["+str(i)+"]="+str(pk[i]))
    out=int(input("Enter the output rate: "))
    bucks=int(input("Enter the bucket size: "))
    curr=0
    for i in range(0,SIZE):
        if pk[i]+curr>bucks:
            if pk[i]>bucks:
                print("Packet is bigger than the bucket")
            else:
                print("Incoming packet cannot be contained in the bucket")

        else:
            curr+=pk[i]
            print("Incoming packet size: "+str(pk[i]))
            print("Packets left to transmit: "+str(curr))
            while curr>0:
                time.sleep(1)
                op=0
                if curr<=out:
                    op=curr
                    curr=0
                else:
                    op=out
                    curr-=out
                print("Packet transmitted: "+str(op))
                print("Byte remaining to transmit: "+str(curr))

main()