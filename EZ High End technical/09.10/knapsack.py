w=int(input())
wt=list(map(int,input().split()))
pr=list(map(int,input().split()))
l=list(zip(wt,pr))
l.sort(key=lambda x:x[1]/x[0],reverse=True)
maxpro=0
for weight,profit in l:
    if weight<=w:
        maxpro+=profit
        w-=weight
    else:
        maxpro+=w*(profit/weight)
        break
print(maxpro)