
# Since we know that this is not divisible by 2, 3, 4, 5, 6, I will start the
# algorithm at the 7th mark.
list = []
number = 600851475143
for x in range(71, 1234169, 2):
    if number % x == 0:
        list.append(x)
        list.append(int(number/x))
    x += 1

list.sort()
list.reverse()

for x in list:
    count = 2
    prime = True
    while count < x:
        if x % count == 0:
            prime = False
            break
        count += 1

    if prime:
        print(x)
        break


a = input()
