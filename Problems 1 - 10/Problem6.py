num1 = 0
num2 = 0
for x in range(1, 101):
    num1 += pow(x, 2)
    num2 += x

num2 = pow(num2, 2)

answer = num2 - num1
print(answer)
