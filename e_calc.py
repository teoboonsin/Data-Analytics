
def factorial_cal(n):
    
    count=2
    i=count-1
    fact=[]
    cal=0
    
    if fact==1:
        i=1
        
    else:   
        while count<=n and count>1:        

            i=i*count
            count+=1
            
    return float(i)

def e_cal(n=100):
    
    dec_pt=int(raw_input('Please input how many decimal points you want in e: '))

    fact=[]
    cal=0.0
    a=0
   
    # sum of 1/factorial n times
    num=0
    while num<n:
        fact.append(1/(factorial_cal(num)))
        num+=1
    
    cal=reduce(lambda x,y: x+y,fact)
        
    return round(cal,dec_pt)
    