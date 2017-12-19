def pi_cal(n=10000):
    
    #Using the Gregory-Leibniz series
    digit=int(raw_input('Please indicate how many decimal points you want Pi to have: '))

    count=0
    i=1
    odd_no=[]
    pos_neg_matrix=[]
    
    # first, generate a series odd numbers using list comprehension
    
    
    while count<n:
        
        odd_no.append(i)
        i+=2
        
        count+=1
                
    
    # if sequence index is even, times -1 to it, or else times +1 to it
    
    for n in odd_no:
        if (odd_no.index(n)+1)%2==0:
            pos_neg_matrix.append(-1)
        else:
            pos_neg_matrix.append(1)
            
    
    # build up pi using the formula up to a certain number of times (n)
         
    a=map(lambda x,y:4.0/(x*y),odd_no,pos_neg_matrix)
    
    return round(sum(a),digit)