
"""
We know if it's divisible by 20, it's also divisible by 2, 4, 5, and 10
If divisible by 18, it's divisible by 2, 3, 6, 9
If divisible by 16, it's divisible by 2, 4, 8
If divisible by 15, it's divisible by 3, 5
If divisible by 14, it's divisible by 2, 7
If divisible by 12, it's divisible by 2, 3, 4, 6
So, we don't really need to check 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
20 - 2, 4, 5, 10
18 - 3, 6, 9
16 - 8
15 -
14 - 7
12 -

We can actually eliminate 15 and 12 since those are covered by other numbers


2 * 3 * 4 * 5 * 6 * 7 * 11 * 13 * 17 * 19
Would be the handwritten answer. However, that's not fun figuring it out
mathmatically. Let's solve it programmically knowing the above dividers and
primes
"""

dividers = [14, 16, 18, 20]
primes = [11, 13, 17, 19]
found = False
counter = 20
while True:
    found = True
    for x in dividers:
        if not counter % x == 0:
            found = False
            break
    if found:
        for x in primes:
            counter *= x
        print(counter)
        break
    counter += 20
