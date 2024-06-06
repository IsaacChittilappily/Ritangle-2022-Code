for a in range(1000):
  for b in range(1000):
    for c in range(1000):
      if (a**2) + (b**2) + (c**2) == 734:
        print(f'({a},{b}), height {c*0.1875}')