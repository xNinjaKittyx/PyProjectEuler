
# Since we know that this is not divisible by 2, 3, 4, 5, 6, I will start the
# algorithm at the 7th mark.
import random


def composite_prime_check(n, k):
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

number = 600851475143
for x in range(3, number // 2,  2):
    if number % x == 0:
        # If the number is divisible...
        # Check if its a prime.
        check_num = number // x
        if composite_prime_check(check_num, 5):
            print(check_num)
            return

