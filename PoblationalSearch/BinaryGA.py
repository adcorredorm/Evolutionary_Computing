from Functions.Binary import max_one
from Agents.BinaryAgent import BinaryAgent
from GeneticAlgorithm import GeneticAlgorithm
from helpers import plot_poblation

class BinaryGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, **kwargs):
    super().__init__(function, ind_size, generations, crossover_rate, BinaryAgent, **kwargs)

if __name__ == '__main__':
  best = BinaryGA(max_one, 60, 100, 0.7).execute(10)[0]
  print(best)