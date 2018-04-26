
def func(some_num):
    y = 0
    while some_num != 1:
        y += 1
        if some_num % 2 == 0:
            some_num //= 2
        else:
            some_num = 3*some_num + 1
    return y

max_y = 0
actual_number = 0
for x in range(2, 1000000):
    result = func(x)
    if result > max_y:
        actual_number = x
        max_y = result
        
    
