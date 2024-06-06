total,denom = 1,1
for i in range(100):
  total = total + (1/(denom*2)) - (1/(denom*4)) - (1/(denom*8))
  denom = denom*8
print(total)

total2, denom2 = 1,1
for i in range(100):
  total2 = total2 - (1/(denom2*2)) + (1/(denom2  *4)) + (1/(denom2*8))
  denom2 = denom2*8
print(total2)
print(total/total2)
print((total/total2)*61)
