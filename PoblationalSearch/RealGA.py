import math
import matplotlib.pyplot as plt
import numpy as np
from Agents.RealAgent import RealAgent
from random import sample
from GeneticAlgorithm import GeneticAlgorithm

class RealGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, _min=0, _max=1, **kwargs):
    super().__init__(function, ind_size, generations, crossover_rate, RealAgent, **kwargs)
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
    cand = []
    for _ in range(len(population)):
      cand.append(min(sample(population, 4)))
    return cand

if __name__ == '__main__':
  def ackley(x, a=20, b=0.2, c=2*math.pi):
    p1 = -a*math.exp(-b*math.sqrt(sum([i**2 for i in x])/len(x)))
    p2 = -math.exp(sum([math.cos(c*i) for i in x])/len(x))
    return p1 + p2 + a + math.exp(1)

  alg = RealGA(ackley, 10, 100, 0.7, -32.768, 32.768)
  pop = []
  for _ in range(1):
    pop.append(alg.execute(100)[1])

  _min = []
  _max = []
  avg = []
  median = []

  pop = np.transpose(pop)
  for gen in pop:
    _min.append(min(gen))
    _max.append(max(gen))
    avg.append(np.average(gen))
    median.append(np.median(gen))

  plt.plot(_min)
  plt.plot(_max)
  plt.plot(avg)
  plt.plot(median)

  plt.show()