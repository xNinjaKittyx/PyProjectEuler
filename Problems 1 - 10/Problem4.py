
# highest = 0
# for x in range(999, 99, -1):
#     for y in range(x, 99, -1):
#         number = x * y
#         numberstring = str(number)
#         if numberstring == numberstring[::-1]
#             if number > highest:
#                 highest = number
#             break
# print(highest)

# One liner
print(max([z for z in (x * y for x in range(999, 99, -1) for y in range(x, 99, -1)) if str(z) == str(z)[::-1]]))
