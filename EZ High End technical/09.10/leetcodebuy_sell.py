def fun(prices):
    maxpro,buy=0,prices[0]
    for i in range(len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        elif prices[i]-buy>maxpro:
            maxpro=prices[i]-buy
    return maxpro

prices=[7,1,5,3,6,4]
print(fun(prices))