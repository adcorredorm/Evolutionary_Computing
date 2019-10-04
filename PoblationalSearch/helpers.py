import matplotlib.pyplot as plt
import numpy as np

def plot_poblation(data):
  _min = []
  _max = []
  avg = []
  median = []

  pop = np.transpose(data)
  for gen in pop:
    _min.append(min(gen))
    _max.append(max(gen))
    avg.append(np.average(gen))
    median.append(np.median(gen))

  plt.plot(_min)
  plt.plot(_max)
  plt.plot(avg)
  plt.plot(median)

  plt.legend(['min', 'max', 'average', 'median'])
  plt.ylabel('fitness')
  plt.xlabel('generations')

  plt.show()