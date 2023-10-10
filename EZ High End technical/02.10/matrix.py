n=int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
def fun(l,i,j,n):
    if l[i][j]==0:
        return
    if l[i][j]==1:
        l[i][j]==0
    if i>0 and i<n-1:
       fun(l,i+1,j,n)
       fun(l,i-1,j,n)
       
    if j>0 and j<n-1:
       fun(l,i+1,j,n)
       fun(l,i-1,j,n)
count=0
for i in range(n):
    for j in range(n):
        if(l[i][j]==1):
            count+=1
        fun(l,i,j,n)
print(count)  