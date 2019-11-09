from random import random, shuffle, sample, randint
from .Algorithm import PoblationalAlgorithm

class GeneticAlgorithm(PoblationalAlgorithm):

  def __init__(self, function, ind_size, generations, crossover_rate, agent, **kwargs):
    super().__init__(function, **kwargs)
    self.ind_size = ind_size
    self.generations = generations
    self.crossover_rate = crossover_rate
    self.agent = agent

  def init_population(self, p_size):
    population = []
    for _ in range(p_size):
      ind = self.agent()
      ind.init(self.ind_size)
      ind.evaluate(self.function)
      population.append(ind)
    return population
  
  def stop(self, population, k):
    return self.generations <= k

  def select_parents(self, population):
    shuffle(population)
    return population

  def descendant(self, population, parents):
    childs = []
    if len(parents) % 2 != 0:
      parents += parents[0]
    for i in range(0, len(parents), 2):
      p1, p2 = parents[i], parents[i+1]
      if random() < self.crossover_rate:
        cut_point = randint(1, len(p1)-1)
        h1 = self.agent(genome=self.cross_parents(p1, p2, cut_point))
        h2 = self.agent(genome=self.cross_parents(p2, p1, cut_point))
        h1.mutate()
        h1.evaluate(self.function)
        h2.mutate()
        h2.evaluate(self.function)
        childs += [h1, h2]
      else:
        childs += [p1, p2]
    return childs
  
  def cross_parents(self, p1, p2, point):
    return p1.genome[:point] + p2.genome[point:]

  def replace(self, population, parents, childs):
    pop = []
    for i in range(len(parents)):
      if childs[i] <= parents[i]: pop.append(childs[i])
      else: pop.append(parents[i])
    return pop

  def grow(self, population, k):
    parents = self.select_parents(population)
    childs = self.descendant(population, parents)
    return self.replace(population, parents, childs)
  