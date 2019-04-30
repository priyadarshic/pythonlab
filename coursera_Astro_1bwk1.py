# Write your calc_stats function here.
import numpy as np

def calc_stats(path):
  
  data = np.loadtxt(path, delimiter=',')
  mean = np.mean(data)
  mean = np.around(mean, decimals=1)
  median = np.median(data)
  median = np.around(median, decimals=1)
  res = (mean, median)
  
  return res

# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
  # Run your `calc_stats` function with examples:
  mean = calc_stats('data2.csv')
  print(mean)
