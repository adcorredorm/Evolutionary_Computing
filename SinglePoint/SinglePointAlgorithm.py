from random import random

class SinglePointAlgorithm:

  def __init__(self, dim, function, descendant, replacement, stop):
    self.dim = dim
    self.function = function
    self.descendant = descendant
    self.replacement = replacement
    self.stop = stop

  def execute(self, _min=0, _max=1):
    k = 0
    vector = [random()*(_max - _min) + _min] * self.dim
    while not self.stop(k, vector, self.function):
      candidate = self.descendant(vector, self.function)
      vector = self.replacement(vector, candidate, self.function)
      k += 1
    
    return vector
