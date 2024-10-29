import random

def is_prime_miller_rabin(n, k=5): 
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    def miller_test(d, n):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        while d != n - 1:
            x = (x * x) % n
            d *= 2
            if x == 1:
                return False
            if x == n - 1:
                return True
        return False
    
    d = n - 1
    while d % 2 == 0:
        d //= 2
    
    for _ in range(k):
        if not miller_test(d, n):
            return False
    return True

print(is_prime_miller_rabin(30)) 
print(is_prime_miller_rabin(3)) 
