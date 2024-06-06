for a in range(-50,50): # brute force method checks the possible values of each letter
  for b in range(-50,50):
    for c in range(-50,50):
      for d in range(-50,50):
        if a + b == abs(1 + c + d) and (a*4) + b == abs(16 + (c*4) + d) and (a*9) + b == abs(81 + (c*9) + d) and (a*16) + b == abs(256 + (c*16) + d):
          # if statement checks if all the conditions are met, as well as simplifying the equation so it is easier to process
          print('Letters abcd are',a,b,c,d,'answer is',int(((a**2)+(b**2)+(c**2)+(d**2))*0.054))