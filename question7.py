# simple brute force question, checking many values of a through f
for a in range(2,100):
  for b in range(2,100):
    for c in range(2,100):
      for d in range(2,100):
        for e in range(2,100):
          for f in range(2,100):
            if a**b == c ** 12 and c**d == e ** 7 and e ** f == a ** 5: # checks if conditions for the question are met
              print(a,b,c,d,e,f)
              break
print('Finished')