from Agents.Agent import BinaryAgent
from random import random, randint, shuffle
from Algorithm import GeneticAlgorithm

class BinaryGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate):
    super().__init__(function, ind_size, generations)
    self.crossover_rate = crossover_rate

  def init_population(self, p_size):
    population = []
    for _ in range(p_size):
      ind = BinaryAgent()
      ind.init(self.ind_size)
      ind.evaluate(self.function)
      population.append(ind)
    return population

  def select_parents(self, population):
    shuffle(population)
    return population

  def descendant(self, population, parents):
    childs = []
    for i in range(0, len(parents), 2):
      p1, p2 = parents[i], parents[i+1]
      if random() < self.crossover_rate:
        cut_point = randint(1, len(p1)-1)
        h1 = BinaryAgent(genome=p1.genome[:cut_point] + p2.genome[cut_point:])
        h2 = BinaryAgent(genome=p2.genome[:cut_point] + p1.genome[cut_point:])
        h1.mutate()
        h1.evaluate(self.function)
        h2.mutate()
        h2.evaluate(self.function)
        childs += [h1, h2]
      else:
        childs += [p1, p2]
    return childs

  def replace(self, population, parents, childs):
    pop = []
    for i in range(len(parents)):
      if childs[i] <= parents[i]: pop.append(childs[i])
      else: pop.append(parents[i])
    return pop

def max_one(ind):
  count = 0
  for value in ind:
    if value: count += 1
  return len(ind) - count

best = BinaryGA(max_one, 60, 100, 0.7).execute(10)
print(best)