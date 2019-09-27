from random import random
from abc import abstractmethod, ABCMeta

class PoblationalAlgorithm(metaclass=ABCMeta):

  @abstractmethod
  def init_population(self, p_size):
    pass

  @abstractmethod
  def stop(self, population, k, function):
    pass

  @abstractmethod
  def grow(self, population, k, function):
    pass

  @abstractmethod
  def select(self, population, function):
    pass

  def __init__(self, p_size, function):
    self.p_size = p_size
    self.function = function

  def execute(self):
    k = 0
    population = self.init_population(self.p_size)
    while not self.stop(population, k, self.function):
      population = self.grow(population, k, self.function)
      k += 1
    return self.select(population, self.function)


class GeneticAlgorithm(PoblationalAlgorithm):

  @abstractmethod
  def select_parents(self, population, function):
    pass

  @abstractmethod
  def descendant(self, population, parents, function):
    pass

  @abstractmethod
  def replace(self, population, parents, childs, function):
    pass

  def __init__(self, p_size, function, ind_size, generations):
    super().__init__(p_size, function)
    self.ind_size = ind_size
    self.generations = generations
  
  def stop(self, population, k, function):
    return k > self.generations

  def grow(self, population, k, function):
    parents = self.select_parents(population, function)
    childs = self.descendant(population, parents, function)
    return self.replace(population, parents, childs, function)
  
  def select(self, population, function):
    index = 0
    value = function(population[0])
    for i in range(1, len(population)):
      v_aux = function(population[i])
      if v_aux < value:
        index = i
        value = v_aux
    return population[index]
