def bi_to_dec(n):
    ans = 0
    i = 0
    while(n != 0):
        temp = n%10
        n //= 10
        if(temp ==1):
            ans = ans+ 2**i 
        i+= 1   
  
    return ans

n = 1011
print(bi_to_dec(n))
    
