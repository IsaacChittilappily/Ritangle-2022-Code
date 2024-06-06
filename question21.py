primes = [2]
primeAM = []
num = 2
for i in range(100000):  # this block of code generates all primes up to 100000
  num += 1
  attempts = 0
  for prime in primes:
    lenprimes = len(primes)
    if num % prime != 0:
      attempts += 1
    if lenprimes == attempts:
      primes.append(num)
      

for prime in primes:
  
  if primes.index(prime) == len(primes)-1: # checks if the penultimate item of the list has been reached and stops code if it is (otherwise the code will throw an index out of range error)
    break
    
  sum = 0 # resets values of sum and product to 0 for each prime
  product = 1
  
  for digit in str(prime): # gets the sum and product of all the digits in the prime
    sum += int(digit) 
    product *= int(digit)
    
  if prime + product + sum == primes[primes.index(prime)+1]: # checks if the prime is an AM prime
    primeAM.append(prime)  # adds am prime to the list

for am in primeAM:
  if str(am).count('0') < 1: # checks if the am prime doesn't contain 0
    print('Answer =',am)
    break