#sliding Window algorithm
l=[2,5,6,7,8,10]
target=7
i=0
j=0
cursum=l[i]
while j<len(l)-1:
    if cursum==target:
        print(i,j,cursum)
        break
    elif cursum>target:
        cursum-=l[i]
        i+=1
    else:
        j+=1
        cursum+=l[j]
        
    
    
    
        
            
