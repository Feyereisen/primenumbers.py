import math

number = 57
divider = [2,3,5,7,13,17]
square = math.sqrt(number)

def prime1(n):
  global square
  global divider
  for i in range(len(divider)):
    if n[abs(i-1)] < square and n[i] > square:
      return "prime"
    else:
      if n % n[i] == 0:
        return "not prime"

def prime(n):
  global square
  global divider
  for i in range(len(divider)):
    if n[abs(i-1)] < square and n[i] > square:
      return "prime"
    else:
      if n % n[i] == 0:
        return "not prime"
  
  while n[len(n)] < square:
    index = 1
    next_prime = n[len(n)] + index
    if prime1(next_prime) == "prime":
      divider.append(next_prime)
      if n % next_prime == 0:
        return "not prime"
    else:
      index +=1
  return "prime"
    
print(f"The number {number} is {prime(number)}")