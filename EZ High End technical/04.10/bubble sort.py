l=list(map(int,input().split()))
flag=False
for i in range(1,n):
    for j in ramge(n-i):
        if l[j]>[j+1]:
            flag=True
            l[j],l[j+1]=l[j+1],l[j]
    if flag==False:
        break
    flag=False
for i in range(n):
    print(l[i])