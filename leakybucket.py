class packet:
    def __init__(self,id,size):
        self.id=id
        self.s=size
    def printpack(self):
        return "Packet "+str(self.id) + " : size "+str(self.s)

def queue(n):
    q=[]
    for i in range(n):
        id=int(input("Enter id of packet"))
        size=int(input("Enter size of packet"))
        q.append(packet(id,size))

    return q
# buffersize=1000
def leakybucket(q):
    leakrate=int(input("Enter leak rate of the bucket"))
    buffsize=int(input("Enter buffer size of the bucket"))
    n=leakrate
    i=0
    while(i<(len(q))):
        # print(i)
        # print(q[i].s)
        if(q[i].s>buffsize):
            print("Bucket is full...packet dropped..")
            i+=1
            continue
        # if(leakrate<q[i].s):
        #     leakrate=n
        #     print("Leak rate is reset to ",n)

        if(leakrate<q[i].s):
            leakrate=n
            print("Leak rate is reset to ",n)
        s=q[i].printpack()+" is sent through the network"
        print( s)
        leakrate=leakrate-q[i].s
        i+=1

        # if(leakrate>q[i].s):
        #     print((q[i].printpack()))
        #     print(" is sent through the network" )
        #     leakrate=leakrate-q[i].s
        #     i+=1

n=int(input("Enter number of packets"))
q=queue(n)
for i in range(len(q)):
    print(q[i].printpack())
leakybucket(q)

