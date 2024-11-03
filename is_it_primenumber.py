import math
import numpy as np

divider = np.loadtxt('divider.txt', dtype=int)

def find_prime(n, dividers):
    square = math.sqrt(n)
    if n == 1:
        return "not prime"
    if n == 2 or n == 3:
        return "prime"
    if n < divider[-1]:
      if n in divider:
        return "prime"
      else:
        return "not prime"
    for i in dividers:
        if i > square:
            return "prime"
        elif n % i == 0:
            return "not prime"
    return "find more primedivider please"

def prime(n, dividers, max_number):
    if find_prime(n, dividers) == "find more primedivider please":
        index = 1
        while dividers[-1] <= max_number:
            next_prime = dividers[-1] + index
            if next_prime in divider and next_prime < divider[-1]:
                return "prime"
            elif next_prime not in divider and next_prime < divider[-1]:
                return "not prime"
            elif find_prime(next_prime, dividers) == "prime":
                dividers = np.append(dividers, next_prime)
                index = 1
                if n % next_prime == 0:
                    return "not prime", dividers
            else:
                index += 1
        return "prime", dividers
    else:
        return find_prime(n, dividers), dividers

prime_numbers = []
max_number = 10000000
for n in range(1, max_number):
    result, divider = prime(n, divider, max_number)
    if result == "prime":
        prime_numbers.append(n)

print(f"There are {len(prime_numbers)} prime numbers between 1 and {max_number}")
np.savetxt('divider.txt', prime_numbers, fmt='%d')
