def fun_split(l):
    for i in range(1,len(l)):
        j=i
        while l[j]<l[j-1] and j>0:
            l[j-1],l[j]=l[j],l[j-1]
            j=j-1
    return l    
l=list(map(int,input().split()))
fun_split(l)
print(l)