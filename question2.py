for a in '1379': # assigns each letter to a number that it could be, eliminating ones that it cannot be.
  for b in '2468':
    for c in '1379'.replace (a,''): # eliminates any options that have been used in previous letters.
      if int (a+b+c) % 3 == 0:
        for d in '2468'.replace (b,''):
          if int (a+b+c+d) % 4 == 0:
            for f in '2468'.replace (b,'').replace (d,''):
               if int (a+b+c+d+'5'+f) % 6 == 0: # letters e and j are guaranteed to be 5 and 0 respectively, so no need to assign them.
                 for g in '1379'.replace (a,'').replace (c,''):
                   if int (a+b+c+d+'5'+f+g) % 7 == 0:
                     for h in '2468'.replace (b,'').replace (d,'').replace (f,''):
                       if int (a+b+c+d+'5'+f+g+h) % 8 == 0:
                         for i in '1379'.replace(a,'').replace(c,'').replace(g,''):
                           if int (a+b+c+d+'5'+f+g+h+i) % 9 == 0:
                             print ('10 digit number =',a+b+c+d+'5'+f+g+h+i+'0') # outputs the 10 digit number.
                             print ('Answer = ',int(int(a+b+c+d+'5'+f+g+h+i+'0')*1.7*10**-7)) # prints the question answer.