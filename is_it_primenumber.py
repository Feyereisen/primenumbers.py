import math

number = 57
divider = [2,3,5,7,13,17]
square = math.sqrt(number)

def prime1(n):
  n = str(n)
  global square
  global divider
  for i in range(len(divider)):
    if int(n[i-1]) < square and int(n[i]) > square:
      return "prime"
    else:
      if n % int(n[i]) == 0:
        return "not prime"

def prime(n):
  n = str(n)
  global square
  global divider
  for i in range(len(divider)):
    if int(n[i-1]) < square and int(n[i]) > square:
      return "prime"
    else:
      if n % int(n[i]) == 0:
        return "not prime"
  
  while int(n[len(n)]) < square:
    index = 1
    next_prime = int(n[len(n)]) + index
    if prime1(next_prime) == "prime":
      divider.append(next_prime)
      if n % next_prime == 0:
        return "not prime"
    else:
      index +=1
  return "prime"
    
print(f"The number {number} is {prime(number)}")