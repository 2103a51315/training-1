def binary_search(l,si,li,target):
    if si<=li:
        mid=(si+li)//2
        if l[mid]==target:
            return mid
        if l[mid]<target:
            return binary_search(l,mid+1,li,target)
        return binary_search(l,mid-1,si,target)
    return mid
l=[4,6,7,2,1]
target=7
res=binary_search(l,0,len(l)-1,target)
print(res)