'''
This was made with the numpy version on Pythonista, which is basically abandonware, so the numpy version outdated.
Takes an array, and divides the value at an index across all other values, then returns the sum of those ratios.
When working with multidimensional arrays, you can determine the array with the greatest ratio sum, either in total or against a certain array.
'''


import numpy as np


__all__ = ['indexRatio', 'allIndicesRatio', '_max', 'forIndex']


def indexRatio(arr, i):
  '''sums the ratio of one index in a 1d against the others'''
  quos = np.divide(arr[i], np.delete(arr, [i]))
  quos = quos[np.isfinite(quos)]
  return np.sum(quos)

def allIndicesRatio(arr):
  '''Finds the ratio sum of all indicies in a 1d array'''
  quos = np.array([
    indexRatio(arr, i) for i in np.arange(len(arr))
  ])
  return np.sum(quos)

def _max(arr, indices=True):
  '''Returns either the rows of the largest allIndiciesRatio sum or the indicies of those rows'''
  rArr = np.array([allIndicesRatio(i) for i in arr])
  arrI = np.where(rArr == np.max(rArr))[0]
  if indices:
    return arrI
  else:
    return arr[arrI]

def forIndex(arr, i, indices=True):
  '''Same as _max except only ratio sums for a specific index in each row'''
  rArr = np.array([indexRatio(subArr, i) for subArr in arr])
  arrI = np.where(rArr == np.nanmax(rArr))[0]
  if indices:
    return arrI
  else:
    return arr[arrI]
  
