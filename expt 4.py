def sqrt(n):
    return n**(0.5)

def sqr(n):
    return n*n

def cube(n):
    return n*n*n
    
def check_for_prime(n):

    if n > 1:
        for i in range(2,n):
            if(n%i == 0):
                print(n,"is not a prime number")
                break
        else :
            print(n,"is a prime number")
    else: 
        print(n,"is not a prime number")

def factorial(n):
    num1 = 1
    for i in range(1,n+1):
        num1 *= i
    print(num1)

def prime_factors(n):
    list1 = []
    for i in range(2,n+1):
        if(n%i == 0):
            for j in range(2,i):
                pass

            else:
                list1.append(i)
    print(list1)

n = 9
print(sqrt(n))
print(sqr(n))
print(cube(n))
check_for_prime(n)
factorial(n)
prime_factors(n)

