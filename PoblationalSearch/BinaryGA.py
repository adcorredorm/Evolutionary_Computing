from Agents.BinaryAgent import BinaryAgent
from GeneticAlgorithm import GeneticAlgorithm

class BinaryGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, **kwargs):
    super().__init__(function, ind_size, generations, crossover_rate, BinaryAgent, **kwargs)

def max_one(ind):
  count = 0
  for value in ind:
    if value: count += 1
  return len(ind) - count

if __name__ == '__main__':
  best = BinaryGA(max_one, 60, 100, 0.7).execute(10)[0]
  print(best)