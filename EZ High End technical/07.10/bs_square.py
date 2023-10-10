def srqt(n,si,li,floor):
    if n<0:
        return -1
    if n==1:
        return 1
    if si<=li:
        mid=(si+li)//2
        sq=mid*mid
        if sq==n:
            return mid
        elif sq<n:
            floor=mid
            return srqt(n,mid+1,li,floor)
        else:
           return srqt(n,si,mid-1,floor)
    return floor
n=int(input())
res=srqt(n,0,n//2,-1)
print(res)