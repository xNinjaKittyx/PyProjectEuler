
total = 0
x = 3
while x < 1000:
    total += x
    x += 3
x = 5
while x < 1000:
    if x % 3 != 0:
        total += x
    x += 5

print(total)
x = input("Press something to exit")
