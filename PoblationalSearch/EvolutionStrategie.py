from random import random, shuffle, sample, randint
from Algorithm import PoblationalAlgorithm
from Agents.RealAgent import RealAgent

class EvolutionStrategie(PoblationalAlgorithm):

  def __init__(self, function, ind_size, generations, **kwargs):
    super.__init__(function, kwargs)
    self.generations = generations
    self.ind_size = ind_size

  def init_population(self, p_size):
    population = []
    for _ in range(p_size):
      ind = RealAgent()
      ind.init(self.ind_size, exogenous=True)
      ind.evaluate(self.function)
      population.append(ind)
    return population

  def stop(self, population, k):
    return self.generations <= k

  def marriage(self, population, size):
    return sample(population, size)

  def recombination(self, parents):
    pass

  def grow(self, population, k):
    for _ in range(len(population)):
      parents = self.marriage(population, 2)
      ind = self.recombination(parents)
      ind.mutate_exogenous()
      population.append(ind)
    return population
    
