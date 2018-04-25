p = 1
n = 1
total = 0

while n < 4000000:
    num = p + n
    if num % 2 == 0:
        total += num
    p = n
    n = num
print(total)
