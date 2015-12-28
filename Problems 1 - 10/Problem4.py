

palindrome = True
highest = 0
for x in range(999, 99, -1):
    for y in range(x, 99, -1):
        number = x * y
        numberstring = str(number)
        for z in range(0, int(len(numberstring)/2)):
            if not numberstring[z] == numberstring[-(z+1)]:
                palindrome = False
                break
        if palindrome:
            if number > highest:
                highest = number
            break
        palindrome = True
print(highest)
