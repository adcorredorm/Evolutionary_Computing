from random import random
from abc import abstractmethod, ABCMeta

class PoblationalAlgorithm(metaclass=ABCMeta):

  @abstractmethod
  def init_population(self, p_size):
    pass

  @abstractmethod
  def stop(self, population, k):
    pass

  @abstractmethod
  def grow(self, population, k):
    pass

  def select(self, population):
    best = population[0]
    for ind in population[1:]:
      if ind < best:
        best = ind
    return best

  def __init__(self, function):
    self.function = function

  def execute(self, p_size):
    k = 0
    population = self.init_population(p_size)
    while not self.stop(population, k):
      population = self.grow(population, k)
      k += 1
      print(self.select(population))
    return self.select(population)


class GeneticAlgorithm(PoblationalAlgorithm):

  @abstractmethod
  def select_parents(self, population):
    pass

  @abstractmethod
  def descendant(self, population, parents):
    pass

  @abstractmethod
  def replace(self, population, parents, childs):
    pass

  def __init__(self, function, ind_size, generations):
    super().__init__(function)
    self.ind_size = ind_size
    self.generations = generations
  
  def stop(self, population, k):
    return k > self.generations

  def grow(self, population, k):
    parents = self.select_parents(population)
    childs = self.descendant(population, parents)
    return self.replace(population, parents, childs)
  