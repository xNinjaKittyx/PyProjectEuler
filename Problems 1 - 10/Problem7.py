
import random

# Let's take our previously used Miller-Rabin check.
def composite_prime_check(n, k=5):
    # Using Miller-Rabin
    if n == 2:
        return True
    if not n % 2:
        return False
    
    r, s = 0, n -1
    while s % 2 == 0:
        r += 1
        s //= 2
        
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True
    
primes = 6
prime = 13
current_num = 15
while primes < 10001:
    if composite_prime_check(current_num):
        prime = current_num
        primes += 1
    current_num += 2

print(prime)
