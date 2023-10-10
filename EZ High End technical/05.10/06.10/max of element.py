def max_element(l,si,li):
    if si==li:
        return l[si]
    mid=(si+li)//2
    return max(max_element(l,si,mid),max_element(l,mid+1,li))
l=list(map(int,input().split()))
res=max_element(l,0,len(l)-1)
print(res)