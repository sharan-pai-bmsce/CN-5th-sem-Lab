def xor1(a,b):
    n=len(a)
    res=""
    for i in range(1,n):
        if a[i]==b[i]:
            res+="0"
        else:
            res+="1"
    return res

def mod2div(divident,divisor):
    divlen=len(divisor)
    temp=divident[0:divlen]
    n=len(divident)
    while divlen<n:
        if temp[0]=='1':
            temp=xor1(temp,divisor)+divident[divlen]
        else:
            temp=temp[1:divlen]+divident[divlen]
        divlen+=1
    if temp[0]=='1':
        temp=xor1(temp,divisor)
    if len(temp)<len(divisor):
        temp='0'+temp
    return temp
        
def encode(data,key):
    append=data+(len(key)*"0")
    rem=mod2div(append,key)
    print("Remaindar: "+rem)
    print("Codeword: "+data+rem)
    rem=mod2div(data+rem,key)
    print(rem)

def polytobin(data):
    keys=[]
    key=""
    for i in range(len(data)):
        if data[i]=='+':
            keys.append(int(key[1:]))
            key=""
            continue
        key+=data[i]
    if key!="":
        keys.append(0)
    bin=""
    j=0
    for i in range(keys[0],-1,-1):
        if keys[j]==i:
            bin+="1"
            j+=1
        else:
            bin+="0"
    return bin

string = input("Enter the key polynomial:\n")
key = polytobin(string)
string = input("Enter the data polynomial:\n")
data = polytobin(string)
print(key, data)
encode(data, key)
