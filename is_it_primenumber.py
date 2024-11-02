import math
import numpy as np

divider = np.loadtxt('divider.txt', dtype =int)

def find_prime(n):
  global divider
  square = math.sqrt(n)
  if n == 1:
    return "not prime"
  if n == 2 or n == 3:
    return "prime"
  for i in divider:
    if i > square:
      return "prime"
    else:
      if n % i == 0:
        return "not prime"
  return "find more primedivider please"

def prime(n):
  global divider
  global max_number
  if find_prime(n) == "find more primedivider please":
    index = 1
    while divider[len(divider)-1] <= max_number:
      next_prime = divider[len(divider)-1] + index
      if find_prime(next_prime) == "prime":
        divider = np.append(divider, next_prime)
        index = 1
        if n % next_prime == 0:
          return "not prime"
      else:
        index +=1
    return "prime"
  else:
    return find_prime(n)

prime_numbers = np.array([])
max_number = 100
for n in range(max_number):
  if prime(n) == "prime":
    prime_numbers = np.append(prime_numbers, n)
print(f"There are {len(prime_numbers)} prime numbers between 1 and {max_number}")
np.savetxt('divider.txt', divider, fmt='%d')
print(divider)