def sortTime(cards): # function calculates time taken to sort a pile
  time = 0
  for x in range(cards+1):
    time += x
  return time

for m in range(1,11): # loops for all m values
  piles = 2**m
  cardsinpile = int(1024/piles)
  centitime = 1000 + (sortTime(cardsinpile) * piles) # adds the sorting time for each pile, plus the initial
  while cardsinpile != 1024: # (until there is only one pile)
    piles /= 2
    cardsinpile *= 2
    centitime += (cardsinpile+1) * int(piles) 
  print('M =',m,'time to sort =', int(centitime*0.01),"seconds,", "answer =",int(centitime*0.00017))