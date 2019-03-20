# optimize
Find the highest ratios of array elements over other array elements

This was made with the numpy version on Pythonista, which is basically abandonware, so the numpy version outdated.
Takes an array, and divides the value at an index across all other values, then returns the sum of those ratios.
When working with multidimensional arrays, you can determine the array with the greatest ratio sum, either in total or against a certain array.

Import with:
  from optimize import optimize
  
# usage
Say you have an array of numbers:
\[\[a, b, c\]
 \[d, e, f\]\]
optimize().ratio
