nums=[2,0,2,1,1,0]
left,i=0,0
right=len(nums)-1
while i<=right:
    if nums[i]==0:
        nums[i],nums[left]=nums[left],nums[i]
        left+=1
        i+=1
    elif nums[i]==1:
        i+=1
    elif nums[i]==2:
        nums[i],nums[right]=nums[right],nums[i]
        right-=1
print(nums)       