from random import random
from SinglePointAlgorithm import SinglePointAlgorithm

class HillClimb(SinglePointAlgorithm):

  @staticmethod
  def hc_descendant(vector, function):
    return [component + (random()*2) - 1 for component in vector]

  @staticmethod
  def hc_replacement(x, y, function):
    if function(x) <= function(y):
      return x
    return y

  def __init__(self, dim, function, stop):
    super().__init__(dim, function, HillClimb.hc_descendant, HillClimb.hc_replacement, stop)
