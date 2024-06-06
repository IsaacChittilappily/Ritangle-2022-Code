primes = [2]
prime5 = []
answer = 999999
for num in range(2,100000): # code produces a list of all 5 digit primes
  attempts = 0
  for prime in primes:
    lenprimes = len(primes)
    if num % prime != 0:
      attempts += 1
    if lenprimes == attempts:
        primes.append(num)
        if num > 10000:
          prime5.append(num)


for a in range(5002): # max possible values for a and b
  for b in range(5001):
    if a <= b:
      continue
      
    else:
      c = int(str(a-b)+str(a+b)) # concatenates the a and b values as in the question

      for prime in prime5:
        if prime == c and c < answer:
          answer,ansA,ansB = c,a,b
          
          print("Answer =",answer,ansA,ansB)