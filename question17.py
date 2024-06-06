import math
for a in range(30):
  for b in range(30):
    for c in range(30):
      if (a**2)+(b**2)+(c**2) == 899 and (2*a*b)+(2*a*c)+(2*b*c) == 1702:
        print(a,b,c)
        a,b,c = math.sqrt(a),math.sqrt(b),math.sqrt(c)
        p = (a+b+c)/2
        print('Answer =',int(math.sqrt(p*(p-a)*(p-b)*(p-c))*1.8))