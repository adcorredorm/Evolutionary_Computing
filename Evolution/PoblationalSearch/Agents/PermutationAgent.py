from random import shuffle, randint
from .Agent import Agent

class PermutationAgent(Agent):

  def init(self, size):
    self.genome = [i for i in range(size)]
    shuffle(self.genome)

  def mutate(self):
    size = len(self.genome)
    p1 = randint(0, size - 1)
    p2 = randint(0, size - 1)
    aux = self.genome[p1]
    self.genome[p1] = self.genome[p2]
    self.genome[p2] = aux

  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def __str__(self):
    S = '['
    for value in self.genome:
      S += str(value) + ','
    return S[:-1] + '] ' + '{:0.2f}'.format(self.fitness)
