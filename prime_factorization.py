def prime_factorization(n):
    
    prime_factors=[]
    
    while True:
        if n%2==0:
            n=n/2
            prime_factors.append(2)
        elif n%3==0:
            n=n/3
            prime_factors.append(3)
    
        else:
            if n!=1:
                prime_factors.append(n)
                break
            else:
                break
    
    return prime_factors
