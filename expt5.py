def reverse_num(n):
    num = 0
    while(n != 0):
        temp = n%10
        n = n//10
        num = num*10 + temp
    return num 

n = 3456
print("The reverse of", n, "is", reverse_num(n))