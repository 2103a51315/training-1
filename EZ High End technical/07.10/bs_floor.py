def bs_floor(l,target,si,li,fl):
    if si<=li:
        mid=(li+si)//2
        if l[mid]==target:
            return l[mid]
        if l[mid] < target:
            fl=l[mid]
            return bs_floor(l,target,mid+1,li,fl)
            return bs_floor(l,target,mid-1,si,fl)
    return fl    
l=[3,6,8,1,5]
n=5
res=bs_floor(l,n,0,len(l)-1,-1)
print(res)
