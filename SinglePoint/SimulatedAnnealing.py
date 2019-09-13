import math
from random import random
from SinglePointAlgorithm import SinglePointAlgorithm

class SimulatedAnnealing(SinglePointAlgorithm):
  @staticmethod
  def st_descendant(vector, function):
    return [component + (random()*2) - 1 for component in vector]

  def cool_scheme(self):
    value = self.temp if self.it == 0 else self.temp * abs(math.sin(self.it)/self.it)
    self.it += 1
    return value

  def st_replacement(self, x, y, function):
    if function(x) <= function(y) or random() <= self.cool_scheme():
      return x
    return y

  def __init__(self, dim, function, stop, init_temp = 1):
    super().__init__(dim, function, SimulatedAnnealing.st_descendant, self.st_replacement, stop)
    self.temp = init_temp
    self.it = 0
