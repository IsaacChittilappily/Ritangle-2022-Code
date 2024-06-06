def heapPermutation(a, size):
    if size == 1:
      x = 4
      partA = ((8*x**2) + (a[0] * x) + (20+a[1])) / (((x**2)+4)*((a[2]*x)+1))
      partB = ((x+a[3])/((x**2)+a[4])) + ((a[5])/((2*x)+1))
      if partA == partB:
        print(a)
    for i in range(size):
        heapPermutation(a, size-1)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
heapPermutation([1,2,3,4,5,6], 6)