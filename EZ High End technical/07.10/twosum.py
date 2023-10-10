l=list(map(int,input().split()))
left=0
right=len(l)-1
target=int(input())
while(left<right):
    if (l[left]+l[right])==target:
        print("found")
        break
    elif (l[left]+l[right])<target:
        left+=1
    else:
        right-=1
else:
    print("not")