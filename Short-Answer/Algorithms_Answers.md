#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(logn)

since the loop increases a by n^2, while comparing it to n^3, the n^2 line will finish faster than the n^3 line. 

b) O(n log n)

the outside for loop will keep running until n is computed.
the inside loop will take significantly less time to compute because it's multiplying by 2 each time

c) O(n)

it's a recursive call and runs through it until n == 0

## Exercise II

Binary Search tree seems like the best way.
It will start in the middle, and then evaluates left and right.
it will cancel out half the options so leaving us with the smallest amount of broken eggs.

runtime: o(logn)
