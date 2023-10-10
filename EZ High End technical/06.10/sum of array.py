'''def sum_array(l):
    sum=0
    for i in range(len(l)):
        sum+=l[i]
    return sum

l=list(map(int,input().split()))
res=sum_array(l)
print(res)'''

def sum_array(l,si,li):
    if si==li:
        return l[si]
    mid=(si+li)//2
    return sum_array(l,si,mid)+sum_array(l,mid+1,li)
l=list(map(int,input().split()))
res=sum_array(l,0,len(l)-1)
print(res)
        
        
        
