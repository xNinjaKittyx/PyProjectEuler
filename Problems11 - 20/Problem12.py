import math

def divisors(num):
    result = {1, num}
    for x in range(2, math.floor(math.sqrt(num))):
        if num % x == 0:
            result.add(x)
            result.add(num // x)
    return result
    
    
total = 1
iteration = 2 
while len(divisors(total)) < 500:
    total += iteration
    iteration += 1
print(total)
