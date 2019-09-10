from random import random
from SinglePointAlgorithm import SinglePointAlgorithm

class SimulatedTempering(SinglePointAlgorithm):
  @staticmethod
  def st_descendant(vector, function):
    return [component + (random()*2) - 1 for component in vector]

  def cool_scheme(self):
    self.temp *= 0.8
    return self.temp

  def st_replacement(self, x, y, function):
    if function(x) <= function(y) or random() <= self.cool_scheme():
      return x
    return y

  def __init__(self, dim, function, stop, init_temp=1):
    self.dim = dim
    self.function = function
    self.stop = stop
    self.temp = init_temp
    self.descendant = SimulatedTempering.st_descendant
    self.replacement = self.st_replacement
    SinglePointAlgorithm(dim, function, self.descendant, self.replacement, stop)
