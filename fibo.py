def fibo_seq():
    
    num=int(raw_input('Please input how many numbers of the Fibonacci sequence you want to generate: '))
    
    i=0
    j=1
    a=0
    fibo=[j]
    count=1
    
    while count<num:
        if num==1:
            break

        else:
            a=i+j
            fibo.append(a)
            i=j
            j=a
            count+=1
    
    return fibo