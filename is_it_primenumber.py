import math
import random

divider = [2, 3]

def find_prime(n):
  global divider
  square = math.sqrt(n)
  if n == 1:
    return "not prime"
  if n == 2 or n == 3:
    return "prime"
  for i in range(len(divider)):
    if divider[i-1] < square and divider[i] > square:
      return "prime"
    else:
      if n % divider[i] == 0:
        return "not prime"
  return "find more primedivider please"

def prime(n):
  global divider
  square = math.sqrt(n)
  if find_prime(n) == "find more primedivider please":
    index = 1
    while divider[len(divider)-1] < square:
      next_prime = divider[len(divider)-1] + index
      if find_prime(next_prime) == "prime":
        divider.append(next_prime)
        index = 1
        if n % next_prime == 0:
          return "not prime"
      else:
        index +=1
    return "prime"
  else:
    return find_prime(n)

prime_numbers = []
max_number = 10000000
for n in range(max_number):
  if prime(n) == "prime":
    prime_numbers.append(n)
print(f"There are {len(prime_numbers)} prime numbers between 1 and {max_number}")