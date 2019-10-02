import math
from Agents.RealAgent import RealAgent
from random import random, randint, shuffle
from Algorithm import GeneticAlgorithm

class RealGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, _min=0, _max=1):
    super().__init__(function, ind_size, generations)
    self.crossover_rate = crossover_rate
    self._min = _min
    self._max = _max

  def init_population(self, p_size):
    population = []
    for _ in range(p_size):
      ind = RealAgent()
      ind.init(self.ind_size, self._min, self._max)
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
        h1 = RealAgent(genome=p1.genome[:cut_point] + p2.genome[cut_point:])
        h2 = RealAgent(genome=p2.genome[:cut_point] + p1.genome[cut_point:])
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

def ackley(x, a=20, b=0.2, c=2*math.pi):
  p1 = -a*math.exp(-b*math.sqrt(sum([i**2 for i in x])/len(x)))
  p2 = -math.exp(sum([math.cos(c*i) for i in x])/len(x))
  return p1 + p2 + a + math.exp(1)

best = RealGA(ackley, 10, 100, 0.7, -32.768, 32.768).execute(500)
print(best)