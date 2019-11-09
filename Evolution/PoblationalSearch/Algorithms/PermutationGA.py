from ..Agents.PermutationAgent import PermutationAgent
from random import random, randint
from .GeneticAlgorithm import GeneticAlgorithm

class PermutationGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, **kwargs):
    super().__init__(function, ind_size, generations, crossover_rate, PermutationAgent, **kwargs)
  
  def cross_parents(self, p1, p2, point):
    child = p1.genome[:point]
    while len(child) < len(p1):
      point = (point + 1)%len(p1)
      if p2.genome[point] not in child:
        child.append(p2.genome[point])
    return child