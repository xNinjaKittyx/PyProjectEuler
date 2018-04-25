
import random

# Let's take our previously used Miller-Rabin check.
def composite_prime_check(n, k=5):
    # Using Miller-Rabin
    if n == 2 or n == 3 or n == 5 or n == 7:
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
    
total = 0
for x in range(2, 2000001):
    if composite_prime_check(x):
        total += x
