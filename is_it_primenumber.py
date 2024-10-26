import math

number = 57
divider = [2,3,5,7,13,17]
square = math.sqrt(number)

def prime1(n):
  n_str = str(n)
  global square
  global divider
  for i in range(len(divider)-1):
    if int(n_str[i-1]) < square and int(n_str[i]) > square:
      return "prime"
    else:
      if n % int(n_str[i]) == 0:
        return "not prime"

def prime(n):
  n_str = str(n)
  global square
  global divider
  for i in range(len(divider)-1):
    if int(n_str[i-1]) < square and int(n_str[i]) > square:
      return "prime"
    else:
      if n % int(n_str[i]) == 0:
        return "not prime"
  
  while int(n_str[len(n_str)]) < square:
    index = 1
    next_prime = int(n_str[len(n_str)]) + index
    if prime1(next_prime) == "prime":
      divider.append(next_prime)
      if n % next_prime == 0:
        return "not prime"
    else:
      index +=1
  return "prime"
    
print(f"The number {number} is {prime(number)}")