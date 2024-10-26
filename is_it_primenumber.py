import math

number = 432668237
divider = [2,3,5,7,13,17]

def find_prime(n):
  global divider
  square = math.sqrt(n)
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
    
print(f"The number {number} is {prime(number)}.")