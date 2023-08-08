machines=[]
network=[]
n=int(input())
for i in range(n):
    a=input()
    network.append(a)
    b=input()
    machines.append(b)
def valid_ip(c):
    k=[]
    for j in c :
        if int(j)>255:
            k.append("Invalid")
    if "Invalid" in k:
        return "Invalid" 
    else:
        return "valid"
def splitting(network):
    result=[]
    for i in network:
        s=i.split(".")
        result.append(valid_ip(s))
    return result    
result=splitting(network)

def seven_occ(network):
    pos=[]
    for IP in network:
        pos.append(IP[0:7])
    return pos 
pos=seven_occ(network)
def localnetwork(pos):
    a=[]+machines
    local1=[]
    local2=[]
    local={}
    for i in range(len(pos)):
        for j in range(len(pos)):
            if pos[i]==pos[j]:
                x=a[i]
                y=a[j]
                if x!=y and (x not in local2 or y not in local1):
                    local1.append(x)
                    local2.append(y) 
                    local[x]=y
    return local 
local=localnetwork(pos)
if "Invalid" in result:
    print("Invalid IP Address")
else:
    p=list(local.keys())
    q=list(local.values())
    for i in range(len(p)):    
        print("Mchines",p[i],"and",q[i],"are on the same local network")
