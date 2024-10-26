import math

n = 57
divider = [2,3,5,7,13,17]

def prime1(n):
  for i in range(len(divider)):
    if n[i-1] < abs(n) and n[i] > abs(n):
      return "prime"
    else:
      if n % n[i] == 0:
        return "not prime"

def prime(n):
  for i in range(len(divider)):
    if n[i-1] < abs(n) and n[i] > abs(n):
      return "prime"
    else:
      if n % n[i] == 0:
        return "not prime"
  
  while n[len(n)] < abs(n):
    index = 1
    next_prime = n[len(n)] + index
    if prime1(next_prime) == "prime":
      divider.append(next_prime)
      if n % next_prime == 0:
        return "prime"
    else:
      index +=1
    
print(f"The number {n} is {prime(n)}")