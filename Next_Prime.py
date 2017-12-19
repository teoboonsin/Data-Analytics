
def is_prime(n):
    
    a=int(round(n**0.5,0))
    ans=True
    
    #check if a number is prime
    
    for num in range(2,a+1):  
        
        if n%num==0:
            ans=False
            break
         
        else:
            continue
    
    return ans
            
             

def gen_prime(n):
    import random
    
    while True:
        
        a=random.randint(1,n+1)
    
        if is_prime(a)==True:
            break
        else:
            continue
    
    return a
 
  


def ask_prime():
    
    prime=0
    prime_list=[]
    
    while True:
        qn=raw_input('Do you want a prime number? (y/n)').lower()
        
        if qn == 'n':
            break
        elif qn=='y':
            qn1=int(raw_input('Please select the integer no that you want your prime number to be up till: '))
            while True:
                prime=gen_prime(qn1)
                if prime not in prime_list:
                    print 'You got a prime number: %i' %prime
                    prime_list.append(prime)
                    break
                else:
                    print 'This number has appeared before. Regenerating a prime number.'
                    continue
            
        else:
            print "Please only input 'y'' or 'n' to the question to indicate yes or no"
            continue
    
    print 'These are your prime numbers: ',prime_list