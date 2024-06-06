def numberToBase(n, b): # this function converts any integer to any given base
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


for m in range(31,10000): # brute forcing values of m and n
  count = 0
  for n in range(2,10000):
    x = 0
    for digit in numberToBase(m,n):
      if digit == 1:
        x+=1
        if x == len(numberToBase(m,n)): # checks if all the digits in the converted number are 1
          count += 1
          if count >= 3:
            print('Answer =',m)         