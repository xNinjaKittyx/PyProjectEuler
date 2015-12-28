import math

n = 10000000


A = [False, False]
count = 2
while count <= n:
    A.append(True)
    count += 1
print("All Values Set To True")

i = 2
while i <= math.sqrt(n):
    if A[i] is True:
        j = pow(i, 2)
        while j <= n:
            A[j] = False
            j += i
    i += 1

count = 0
prime = 1
for x in A:
    if x is True:
        if prime == 10001:
            print("Prime #{0} : {1}".format(prime, count))
        prime += 1
    count += 1

input()
