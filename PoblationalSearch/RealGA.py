import Functions.Real as func
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

if __name__ == '__main__':
  best = RealGA(func.ackley, 10, 100, 0.7, -32.768, 32.768).execute(100)[0]
  print(best)