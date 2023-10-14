l=[2,3,0,4,6,3,2,1]
maxele=max(l)
for i in range(maxele,0,-1):
    print(f"{i:2d} | ",end=" ")
    for j in l:
        if j>=i:
            print(" x ",end="")
        else:
            print("   ",end="")
    print()