def num_component(num):
    
    import collections
    
    int_num=int(num)
    
    if int_num==0:
        dec_num=int(round(num,2)*100)
    else:
        dec_num=int(round((num-int_num),2)*100)
    
    store_digit=collections.OrderedDict()
    
    notes={'millions':1000000,'hundred-thousands':100000,'ten-thousands':10000,'thousands':1000,'hundreds':100,'tens':10, 'ones':1}
    coins={'ten_cts':10, 'one_ct':1}
    
    # integer component
    temp=int_num
    count=1
    
    while int_num>0:
        
        if int_num/10>0:
            count*=10
            int_num=int(int_num/10)
        
        else:
            
            for name, num in notes.iteritems():
                if num == count:
                    store_digit[name]=int_num

            int_num=temp-count*int_num
            count=1
            temp=int_num
    
    
    
    #dec component
    temp_dec=dec_num
    
    count=1
    
    while dec_num>0:
        if dec_num/10>0:
            count*=10
            dec_num=int(dec_num/10)
        else:
            for name, num in coins.iteritems():
                if num==count:
                    store_digit[name]=dec_num
                
            dec_num=temp_dec-count*dec_num
            count=1
            temp_dec=dec_num
    
    
    
    return store_digit


def Change_Return():
    
    cost=float(raw_input('Please input the cost: '))
    money=float(raw_input('Please input the amount of money given: '))
    
    while True:
        if money<cost:
            print 'You did not give enough money!'
            money=float(raw_input('Please input the amount of money given: '))
        
        else:
    
            dollars_and_cents=num_component(money-cost)
            break
       
    return dollars_and_cents



#main program


Change_Return()