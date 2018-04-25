# Brute Force Method:
def brute_force():
  for x in range(1, 1001):
      for y in range(1, 1001):
          for z in range(1, 1001):
              if x + y + z == 1000:
                  l = sorted([x**2, y**2, z**2])
                  if l[0] + l[1] == l[2]:
                      print(l)
                      return 

# I don't know how to prove it, but if you knew that the numbers are going to be divisibles of 5.
def brute_force():
  for x in range(1, 1001, 5):
      for y in range(1, 1001, 5):
          for z in range(1, 1001, 5):
              if x + y + z == 1000:
                  l = sorted([x**2, y**2, z**2])
                  if l[0] + l[1] == l[2]:
                      print(l)
                      return 
# Solves quite quickly.
