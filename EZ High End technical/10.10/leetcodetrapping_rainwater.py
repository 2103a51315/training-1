def fun(height):
    if not height:return True
    l=0
    r=len(height)-1
    maxl=height[l]
    maxr=height[r]
    res=0
    while l<r:
        if maxl<maxr:
            l+=1
            maxl=max(maxl,height[l])
            res+=maxl-height[l]
        else:
            r-=1
            maxr=max(maxr,height[r])
            res+=maxr-height[r]
    return res
height=[4,2,0,3,2,5]
print(fun(height))