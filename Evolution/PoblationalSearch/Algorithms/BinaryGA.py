from ..Agents.BinaryAgent import BinaryAgent
from .GeneticAlgorithm import GeneticAlgorithm

class BinaryGA(GeneticAlgorithm):
  
  def __init__(self, function, ind_size, generations, crossover_rate, **kwargs):
    super().__init__(function, ind_size, generations, crossover_rate, BinaryAgent, **kwargs)
