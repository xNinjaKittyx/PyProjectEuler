"""Finding the sum of all even fibonnachi numbers under 4 million"""
fibnum = [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

while True:
    num = fibnum[-2] + fibnum[-1]
    if num > 4000000:
        break
    fibnum.append(num)

counter = 1
last = len(fibnum)
total = 0
while counter < last:
    total += fibnum[counter]
    counter += 3
print(total)

a = input()
