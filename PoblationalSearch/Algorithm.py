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
    return min(population)

  def __init__(self, function):
    self.function = function

  def execute(self, p_size):
    k = 0
    stats = []
    population = self.init_population(p_size)
    while not self.stop(population, k):
      population = self.grow(population, k)
      stats.append(self.select(population).fitness)
      k += 1
    return (self.select(population), stats)


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
    return self.generations <= k

  def grow(self, population, k):
    parents = self.select_parents(population)
    childs = self.descendant(population, parents)
    return self.replace(population, parents, childs)
  