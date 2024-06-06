maxProduct = 0 # creates a variable to hold the max product found
def heapPermutation(a, size): # uses heaps algorithm to generate all permutations of the numbers
    global maxProduct
    if size == 1:
      num1 = int(a[0]+a[1]) # assigns the numbers to a variable
      num2 = int(a[2]+'5'+a[3])
      num3 = int(a[4]+'4'+a[5])
      if (num1+num3)/2 == num2: # checks if numbers are in arithmetic progression
        if num1*num2*num3 > maxProduct: # checks if the product of those numbers is higher than the last max product
          maxProduct = num1*num2*num3 # if they are, reassigns max product to new product
    for i in range(size):
        heapPermutation(a, size-1)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]

heapPermutation(['1','2','3','4','5','6'], 6)
print('Product is',(maxProduct),', answer is',int(maxProduct*3.8*10**-6)) # outputs the answer