def sieveOfEratosthenes(num):
    prime=[True for i in range(num+1)]
    p=2
    while(p*p<=num):
        if prime[p]:
            for i in range(p*p,num,p):
                prime[i]=False
        p+=1
    for p in range(2,num):
        if prime[p]:
            print(p,end=" ")
num=30
sieveOfEratosthenes(num)
        
    
        
    