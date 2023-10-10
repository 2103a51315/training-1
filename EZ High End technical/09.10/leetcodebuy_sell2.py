def fun(prices):
    maxpro,buy=0,prices[0]
    for i in range(1,len(prices)):
        if prices[i]<buy:
            buy=prices[i]
        elif prices[i] > prices[i-1]:
            maxpro+=prices[i]-prices[i-1]
    return maxpro
prices=[2,5,6,8,4]
print(fun(prices))

  