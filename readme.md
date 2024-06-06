# Ritange Code
![Alt text](https://pbs.twimg.com/media/FdlItjmXgAIv_XO.jpg)
This project was created for the integral maths competition, Ritangle 2022. The files are labelled with the code I wrote for each respective question, they can all be run from main.py.

The code that I reused the most was Heaps Algorithm for permutations:

        # finds all possible arrangements of an array
    def heapPermutation(a, size):
        # if size becomes 1 then prints the obtained permutation
        if size == 1:
            print(a)
            return
        for i in range(size):
            heapPermutation(a, size-1)
          
            # if size is odd, swap 0th i.e (first)
            # and (size-1)th i.e (last) element
            # else If size is even, swap ith
            # and (size-1)th i.e (last) element
            if size & 1:
              
                a[0], a[size-1] = a[size-1], a[0]
            else:
              
                a[i], a[size-1] = a[size-1], a[i]
    # Driver code
    a = [1,2,3,4]
    heapPermutation(a, 4)

Many of the questions required me to brute force check all possible options for variables, with a given set of numbers that they could be. This code was the backbone of my algorithms to do most of the questions, as it lets me find those options efficiently.
