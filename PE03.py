import math

def is_prime(n):
    for i in range(2,int(math.ceil(math.sqrt(n)))+1):
        if n % i == 0:
            return False
    else:
        return True



def euler_prime(n):
    primefactors = []
    for i in range(1,int(math.ceil(math.sqrt(n)))):
        if is_prime(i) and (n%i ==0):
            primefactors.append(i)
    print(max(primefactors))

print(euler_prime(600851475143))



