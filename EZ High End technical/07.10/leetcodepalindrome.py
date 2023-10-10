def has_palin(s):
    def ispalin_rev(left,right):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return s[left+1:right]
    res=[]
    for i in range(len(s)):
        pali1=ispalin_rev(i,i)
        if len(pali1)>1:
            res.append(pali1)
        pali2=ispalin_rev(i,i+1)
        if len(pali2)>1:
            res.append(pali2)
    return res
s=input()
result=has_palin(s)
print(result)
    