#Tower of hanoi
def toh(n,src,aux,dest):
    if(n==1):
        print("desk moved to "+src+" to " +dest)
        return
    toh(n-1,src,dest,aux)
    print("desk moved to "+src+" to " +dest)
    toh(n-1,aux,src,dest)

n=int(input())
toh(n,'src','aux','dest')
    