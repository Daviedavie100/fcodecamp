# import numpy library

import numpy as np

# define function

def calculate(lst):

'''Using numpy to calculate mean, standard deviation, variance, minimum, maximum and sum
and if the length of the input list is not equal to 9, then raise a ValueError with message'''

  if len(lst) != 9:
    raise ValueError ('List must contain nine numbers.')
  else:
    mtx=np.array(lst).reshape((3,3))
    calculations={
      'mean': [list(np.mean(mtx,axis=0)), list(np.mean(mtx,axis=1)), np.mean(mtx)],
      'variance': [list(np.var(mtx,axis=0)), list(np.var(mtx,axis=1)), np.var(mtx)],
      'standard deviation': [list(np.std(mtx,axis=0)), list(np.std(mtx,axis=1)), np.std(mtx)],
      'max': [list(np.max(mtx,axis=0)), list(np.max(mtx,axis=1)), np.max(mtx)],
      'min': [list(np.min(mtx,axis=0)), list(np.min(mtx,axis=1)), np.min(mtx)],
      'sum': [list(np.sum(mtx,axis=0)), list(np.sum(mtx,axis=1)), np.sum(mtx)]
    }
  return calculations
calculate([10,1,2,3,4,5,6,7,8])
