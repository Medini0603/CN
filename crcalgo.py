def xor(dividend,divisor):
    res=[]
    for i in range(1,len(divisor)):
        if(dividend[i]==divisor[i]):
            res.append("0")
        else:
            res.append("1")
    temp="".join(str(x) for x in res)
    return temp

def mod2div(dividend,divisor):
    pick=len(divisor)
    divid=dividend[0:pick]
    while(pick<len(dividend)):
        print(divid)
        if(divid[0]=='1'):
            divid=xor(divisor,divid)+dividend[pick]
        else:
            divid=xor("0"*pick,divid)+dividend[pick]

        pick+=1

    if(divid[0]=='1'):
        divid=xor(divisor,divid)
    else:
        divid=xor("0"*pick,divid)

    rem=divid
    return rem

def crc(key,msg):

    msg2=msg+"0"*(len(key)-1)
    rem=mod2div(msg2,key)

    res=msg+rem
    print(rem)
    print(res)

data=(input("Enter data"))
key=(input("Enter key"))
crc(key, data)

rdata=(input("Enter recieved data"))
rem=mod2div(rdata,key)
print(rem)
if(rem=="0"*(len(key)-1)):
    print("No error")
else:
    print("Error")


