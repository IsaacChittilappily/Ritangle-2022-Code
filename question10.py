import math
largearea = 0
smallarea = 9999999

def heapPermutation(a, size):
    global smallarea
    global largearea
    if size == 1:
      sideA, sideB, sideC = int(a[0]+a[1]+a[2]), int(a[3]+a[4]+a[5]), int(a[6]+a[7]+a[8]) # defines the sides from permutation
      p = (sideA+sideB+sideC)/2 # gets the semiperimeter (perimeter/2) which is used in Herons formula
      
      if sideA + sideB > sideC and sideA + sideC > sideB and sideB + sideC > sideA: # checks if it is a valid triangle
        area = math.sqrt(p*(p-sideA)*(p-sideB)*(p-sideC)) # uses Herons formula for area of a triangle
        
        if area < smallarea: 
          smallarea = area # records smallest and largest areas found

        if area > largearea:
          largearea = area
          
        return

    for i in range(size):
        heapPermutation(a, size-1)
        if size & 1:
            a[0], a[size-1] = a[size-1], a[0]
        else:
            a[i], a[size-1] = a[size-1], a[i]
          
a = ['1','2','3','4','5','6','7','8','9']
heapPermutation(a, 9)
print(f'Triangle P = {int(largearea)}, Triangle Q = {int(smallarea)}, answer = {int(((largearea/smallarea))*0.081)}')